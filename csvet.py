import os
import time
import google.generativeai as genai
import subprocess

genai.configure(api_key="AIzaSyDNsSei1w6Q4Oa6iSz2ZWskDcXkf9GvErI")

def upload_to_gemini(path, mime_type="video/mp4"):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def wait_for_files_active(files):
    """Waits for the given files to be active."""
    print("Waiting for file processing...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    print("...all files ready")
    print()

# Prompt user for the video file path
file_path = input("Enter the path to the video file (e.g., 'vjti.mp4'): ")

# Extract the file name from the file path (without extension)
file_name = os.path.basename(file_path)

# Upload the user-provided file
files = [
    upload_to_gemini(file_path),  # MIME type is fixed to "video/mp4"
]

# Wait for the files to become active
wait_for_files_active(files)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
     system_instruction=f"\"I need a Python script using the MoviePy library that performs the following tasks:\n\n"
                        f"Load a video file '{file_name}' correctly using VideoFileClip.\n\n"
                        "Remove unnecessary and repetitive clips: Define subclips within valid timestamps, ensuring that there are no overlapping or redundant time ranges. Each subclip should serve a purpose, so remove any clips that are not required.\n\n"
                        "Extract timestamps: Ensure the correct timestamps are extracted, taking into account the actual duration of the video. If the video is 19 seconds, timestamps should be within the valid range of 0-19 seconds.\n\n"
                        "Apply transitions: Apply transitions such as fadein or fadeout between clips. Ensure that transitions are properly applied without any errors due to invalid references or durations. The transitions should also respect the clip's start and end time.\n\n"
                        "Apply video effects: Implement video effects like speed adjustment (speedx) if needed.\n\n"
                        "Concatenate clips: Combine the subclips into a final video and save it as edited_video.mp4.\n\n"
                        "Extract highlight clips: Based on predefined valid timestamps, extract highlights from the video and save them as highlights_video.mp4.\n\n"
                        "Code Requirements:\n\n"
                        "Ensure proper imports and use only valid MoviePy methods.\n"
                        "The script should handle transitions without errors (e.g., no incorrect object references).\n"
                        "Remove redundant or unused code to ensure clarity and efficiency.\n"
                        "Write the script in a modular and clean format, with clear comments for each step.\n"
                        "Test and verify the syntax and functionality of the script to ensure there are no trivial errors.\n"
                        "Ensure that timestamps used for subclips are valid within the video’s total duration, and calculations are based on the actual video length.\n\n"
                        "Sample Data:\n\n"
                        "The sample video has a duration of 19 seconds. Therefore, timestamps like {{\"start\": 0, \"end\": 5}} should be correctly defined within this 19-second range. Ensure that the subclip timestamps are adjusted based on the actual video length and that no clips exceed the video duration.\n"
                        "Considerations:\n\n"
                        "Ensure that the final video is properly concatenated, with transitions applied smoothly.\n"
                        "Make sure the highlight clips are extracted accurately based on valid timestamps.\n"
                        "Output: The final output should include:\n\n"
                        "edited_video.mp4: The full video with transitions and effects applied.\n"
                        "highlights_video.mp4: The video containing only the highlight clips extracted based on the timestamps.\"\n\n"
                        "Just give the code, no explanations.",
)

# Start the chat session with the model
chat_session = model.start_chat()

# Send the input prompt to generate the Python script
response = chat_session.send_message("INSERT_INPUT_HERE")

# Assuming `response.text` contains the script content
response_text = response.text

# Define the path for the new Python file
output_file_path = 'output.py'

# Save the content to a Python file
with open(output_file_path, 'w') as f:
    f.write(response_text)

print(f"Script saved to {output_file_path}")

# Step 1: Read the content of the saved Python script
with open(output_file_path, 'r') as f:
    lines = f.readlines()

# Step 2: Remove the first and last lines
if len(lines) > 1:
    lines = lines[1:-1]  # Remove the first and last lines

# Step 3: Write the modified content back to the file
with open(output_file_path, 'w') as f:
    f.writelines(lines)

print(f"Modified script written to {output_file_path}")

# Step 4: Run the modified Python script
try:
    subprocess.run(['python', output_file_path], check=True)
    print(f"Script {output_file_path} executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing {output_file_path}: {e}")
