import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def apply_color_grading(clip):
    """
    Apply color grading effects to a video clip.
    :param clip: The video clip to process.
    :return: Color-graded clip.
    """
    return clip.fx(vfx.colorx, 1.2)  # Adjust color intensity

def add_random_transition(clips):
    """
    Add random transitions between clips.
    :param clips: List of video clips.
    :return: Concatenated video with transitions.
    """
    transitions = [
        lambda clip: clip.crossfadein(1),
        lambda clip: clip.fadein(1),
        lambda clip: clip.fadeout(1),
        lambda clip: clip.fx(vfx.lum_contrast, 0.2, 0.2),
    ]
    
    final_clips = []
    for i, clip in enumerate(clips):
        final_clips.append(clip)
        if i < len(clips) - 1:  # Add transition only between clips
            transition = random.choice(transitions)
            final_clips.append(transition(clips[i+1]))
    
    return concatenate_videoclips(final_clips, method="compose")

def process_video(input_path, output_path):
    """
    Process the input video to color grade and add transitions.
    :param input_path: Path to the input video.
    :param output_path: Path to save the processed video.
    """
    # Load the input video
    clip = VideoFileClip(input_path)
    
    # Split the video into scenes (for demonstration, split into 3 equal parts)
    print("Splitting video into scenes...")
    duration = clip.duration
    scenes = [
        clip.subclip(0, duration / 3),
        clip.subclip(duration / 3, 2 * duration / 3),
        clip.subclip(2 * duration / 3, duration)
    ]
    
    # Apply color grading to each scene
    print("Applying color grading...")
    graded_scenes = [apply_color_grading(scene) for scene in scenes]
    
    # Add randomized transitions between scenes
    print("Adding transitions...")
    final_clip = add_random_transition(graded_scenes)
    
    # Write the final output video
    print("Writing the final video...")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print("Video processing complete!")

# Input and output video paths
input_video = "nature.mp4"  # Replace with your input video file
output_video = "output_video.mp4"  # Output file path

# Run the video processing function
process_video(input_video, output_video)
