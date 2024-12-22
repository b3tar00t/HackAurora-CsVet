import os
import random
import numpy as np
import cv2
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, CompositeVideoClip
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.fadein import fadein
from moviepy.editor import ImageClip
from scenedetect import detect, ContentDetector, AdaptiveDetector
from vidstab import VidStab
from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range
import torch
import torchvision.transforms as transforms
from PIL import Image, ImageEnhance
from scipy.signal import medfilt
import librosa
import warnings
from typing import List, Tuple, Dict, Optional, Union
import logging

# Custom implementation of reverse effect
def reverse_clip(clip):
    """Custom implementation of video reversal."""
    return clip.set_duration(clip.duration).fl_time(lambda t: clip.duration - t)

class AdvancedVideoEnhancer:
    def __init__(self, input_path: str, enhance_level: str = 'medium'):
        """
        Initialize the video enhancer with various enhancement levels.
        
        Args:
            input_path: Path to input video
            enhance_level: 'light', 'medium', or 'heavy' enhancement
        """
        self.input_path = input_path
        self.enhance_level = enhance_level
        self.stabilizer = VidStab()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Enhancement parameters based on level
        self.enhancement_params = {
            'light': {
                'color_boost': 1.1,
                'contrast': 1.1,
                'brightness': 1.05,
                'stabilization_window': 20,
                'transition_duration': 0.5
            },
            'medium': {
                'color_boost': 1.2,
                'contrast': 1.2,
                'brightness': 1.1,
                'stabilization_window': 30,
                'transition_duration': 0.8
            },
            'heavy': {
                'color_boost': 1.3,
                'contrast': 1.3,
                'brightness': 1.15,
                'stabilization_window': 40,
                'transition_duration': 1.0
            }
        }
        
        # Visual effects
        self.visual_effects = [
            'cinematic',
            'vintage',
            'warm',
            'cool',
            'dramatic',
            'vibrant'
        ]

    def apply_brightness(self, clip, brightness_factor: float):
        """Manually adjust brightness of a video clip using PIL."""
        def brightness_frame(get_frame, t):
            frame = get_frame(t)
            pil_image = Image.fromarray(frame)
            enhancer = ImageEnhance.Brightness(pil_image)
            pil_image = enhancer.enhance(brightness_factor)
            return np.array(pil_image)
        
        return clip.fl(lambda gf, t: brightness_frame(gf, t))

    def process_video(self) -> str:
        """Process the video based on enhancement level."""
        clip = VideoFileClip(self.input_path)
        
        # Apply color enhancement
        params = self.enhancement_params.get(self.enhance_level, self.enhancement_params['medium'])
        clip = clip.fx(vfx.colorx, params['color_boost'])
        
        # Apply contrast enhancement
        clip = clip.fx(vfx.lum_contrast, contrast=params['contrast'])
        
        # Apply brightness enhancement using the custom method
        clip = self.apply_brightness(clip, params['brightness'])
        
        # Stabilize the video
        stabilized_path = "temp_stabilized_video.mp4"
        stabilization_result = self.stabilizer.stabilize(input_path=self.input_path, output_path=stabilized_path)

        if not os.path.exists(stabilized_path):
            raise ValueError("Stabilization failed, output file does not exist.")
        
        stabilized_clip = VideoFileClip(stabilized_path)
        
        # Apply transitions (e.g., fade in/out)
        stabilized_clip = stabilized_clip.fx(fadein, duration=params['transition_duration'])
        stabilized_clip = stabilized_clip.fx(fadeout, duration=params['transition_duration'])
        
        # Save the processed video
        output_path = self.input_path.replace('.mp4', f'_enhanced_{self.enhance_level}.mp4')
        stabilized_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        return output_path

def enhance_video(input_path: str = None, enhancement_level: str = 'medium') -> str:
    """
    Main function to enhance a video file with specified enhancement level.
    
    Args:
        input_path: Optional path to the input video file
        enhancement_level: 'light', 'medium', or 'heavy'
        
    Returns:
        Path to the enhanced video file
    """
    if input_path is None:
        input_path = input("Please enter the path to your video file: ").strip()
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Video file not found: {input_path}")
    
    enhancer = AdvancedVideoEnhancer(input_path, enhancement_level)
    output_path = enhancer.process_video()
    
    return output_path

if __name__ == "__main__":
    try:
        print("Welcome to Advanced AI Video Editor!")
        print("\nEnhancement Levels:")
        print("1. Light - Subtle improvements")
        print("2. Medium - Balanced enhancements")
        print("3. Heavy - Dramatic enhancements")
        
        level_choice = input("\nChoose enhancement level (1/2/3) [default=2]: ").strip()
        level_map = {'1': 'light', '2': 'medium', '3': 'heavy'}
        enhancement_level = level_map.get(level_choice, 'medium')
        
        enhanced_video_path = enhance_video(enhancement_level=enhancement_level)
        print(f"\nVideo enhancement complete!")
        print(f"Enhanced video saved to: {enhanced_video_path}")
    except Exception as e:
        print(f"\nError during video enhancement: {str(e)}")
    finally:
        print("\nVideo processing finished.")
