from moviepy import VideoFileClip

def crop_video(input_file, timestamp_1, timestamp_2, output_file):
    # Load the video clip
    video = VideoFileClip(input_file)

    # If timestamp 1 is not provided, set it to 0
    if timestamp_1 is None:
        timestamp_1 = 0

    # If timestamp 2 is not provided, set it to the last second of the clip
    if timestamp_2 is None:
        timestamp_2 = video.duration

    # Crop the video to the specified timestamps
    cropped_video = video.subclipped(timestamp_1, timestamp_2)

    # Write the cropped video to an output file
    cropped_video.write_videofile(output_file, codec="libx264")

    # Close the video objects to release resources
    video.close()
    cropped_video.close()

def main():
    # Get user inputs for video file, timestamps, and output file
    input_file = input("Enter the path to the input video file: ")

    # Get timestamp 1 and handle default (None -> 0)
    timestamp_1_input = input("Enter the start timestamp (in seconds) or press Enter to use 0: ")
    timestamp_1 = float(timestamp_1_input) if timestamp_1_input else 0

    # Get timestamp 2 and handle default (None -> last second of the clip)
    timestamp_2_input = input("Enter the end timestamp (in seconds) or press Enter to use the last second: ")
    timestamp_2 = float(timestamp_2_input) if timestamp_2_input else None

    output_file = input("Enter the path for the output video file: ")

    # Call the function to crop the video
    crop_video(input_file, timestamp_1, timestamp_2, output_file)

if __name__ == "__main__":
    main()
