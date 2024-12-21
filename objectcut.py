import cv2
import numpy as np
import scenedetect
from scenedetect import open_video, ContentDetector

def compare_frames(frame1, frame2):
    """
    Compares two frames to check if they are different using ORB and BFMatcher.
    Returns True if frames are different, otherwise False.
    """
    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and compute descriptors
    kp1, des1 = orb.detectAndCompute(frame1, None)
    kp2, des2 = orb.detectAndCompute(frame2, None)

    # If either of the descriptors is None (no keypoints found), return False
    if des1 is None or des2 is None:
        return False

    # Use the Brute-Force Matcher to match descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Check if there are enough matches to consider the frames as different
    if len(matches) > 10:  # Adjust this threshold as needed
        return True  # Frames are different
    else:
        return False  # Frames are too similar

def save_frame(video_path, frame_num, filename):
    """
    Saves a specific frame from the video to an image file.
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Set the video to the specific frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    # Read the frame
    ret, frame = cap.read()

    # If the frame is read successfully, save it
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()

def detect_scenes_and_extract_frames(video_path):
    """
    Detects scene changes in the video and extracts the first and last frame of each scene using pyscenedetect.
    """
    # Open the video file with scenedetect
    video = open_video(video_path)
    scene_manager = scenedetect.SceneManager()
    
    # Add the ContentDetector to detect scenes
    scene_manager.add_detector(ContentDetector())

    # Detect scenes
    scene_manager.detect_scenes(video)

    # Get the list of scene cuts
    scene_list = scene_manager.get_scene_list()

    print(f"Detected {len(scene_list)} scenes")

    # Open the video file with OpenCV for frame extraction
    cap = cv2.VideoCapture(video_path)
    
    # Get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Loop through the scenes and extract the relevant frames
    for i in range(len(scene_list) - 1):
        # Get the scene start and end times (scene_list contains tuples of (start_time, end_time))
        current_scene_start_time = scene_list[i][0]
        next_scene_start_time = scene_list[i + 1][0]

        # Convert FrameTimecode to seconds before multiplying by fps
        current_scene_start_seconds = current_scene_start_time.get_seconds()
        next_scene_start_seconds = next_scene_start_time.get_seconds()

        # Convert times to frame numbers
        current_scene_start_frame = int(current_scene_start_seconds * fps)
        next_scene_start_frame = int(next_scene_start_seconds * fps)

        print(f"Processing scene {i+1}: Frame {current_scene_start_frame} to {next_scene_start_frame}")

        # Extract and save the first and last frames of the current and next scenes
        save_frame(video_path, current_scene_start_frame, f"scene_{i+1}_first_frame.jpg")
        save_frame(video_path, next_scene_start_frame, f"scene_{i+1}_last_frame.jpg")

        # Load the saved frames for comparison
        current_frame = cv2.imread(f"scene_{i+1}_first_frame.jpg")
        next_frame = cv2.imread(f"scene_{i+1}_last_frame.jpg")

        # Compare frames using the object detection logic
        if compare_frames(current_frame, next_frame):
            print(f"Scene {i+1}: Frames are different, extracted key frames.")
        else:
            print(f"Scene {i+1}: Frames are too similar, skipped.")

    cap.release()

def main():
    # Ask the user for the video path
    video_path = input("Enter the path to the video: ")

    # Detect scene changes and extract frames
    detect_scenes_and_extract_frames(video_path)

if __name__ == "__main__":
    main()
