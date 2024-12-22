from moviepy import VideoFileClip, concatenate_videoclips
import os

def merge_clips():
    try:
        print("Starting the video merging process.")

        # Step 1: Take input for the number of clips
        while True:
            try:
                num_clips = int(input("Enter the number of video clips to merge: "))
                if num_clips < 2:
                    print("You need at least 2 clips to merge. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        clips = []

        # Step 2: Take input for each clip and load it
        for i in range(num_clips):
            while True:
                clip_path = input(f"Enter the path for clip {i + 1}: ")

                if not os.path.exists(clip_path):
                    print(f"File not found: {clip_path}. Please try again.")
                    continue

                try:
                    clip = VideoFileClip(clip_path)
                    clips.append(clip)
                    break
                except Exception as e:
                    print(f"Error loading clip {clip_path}: {e}. Please try again.")

        # Step 3: Merge the clips
        try:
            print("Merging clips...")
            merged_clip = concatenate_videoclips(clips, method="compose")

            # Step 4: Save the output
            while True:
                output_path = input("Enter the output file name (e.g., output.mp4): ")
                if not output_path.strip():
                    print("Output file name cannot be empty. Please try again.")
                    continue

                try:
                    merged_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
                    print(f"Merged video saved as {output_path}")
                    break
                except Exception as e:
                    print(f"Error saving the file: {e}. Please try again.")
        except Exception as e:
            print(f"Error during merging: {e}")
    finally:
        # Close all clips to release resources
        print("Releasing resources...")
        for clip in clips:
            clip.close()

if __name__ == "__main__":
    merge_clips()
