import os
import cv2
from datetime import timedelta

import cv2
import os
from datetime import timedelta

def extract_frames(video_path, output_folder, frame_rate=1):
    """
    Extract frames from a video at the specified frame rate.

    :param video_path: Path to the video file
    :param output_folder: Folder to save the extracted frames
    :param frame_rate: Number of frames to extract per second
    """
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print(f"Failed to open video: {video_path}")
        return

    # Get video name
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    print(f"Start extracting from video: {video_name}")

    # Get video properties
    fps = capture.get(cv2.CAP_PROP_FPS)
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Ensure valid frame rate
    if fps == 0 or frame_rate > fps:
        print(f"Invalid frame rate or FPS for video: {video_path}")
        return

    # Calculate the interval between saved frames
    interval = int(fps // frame_rate)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = capture.read()
        if not ret:  # End of video
            break

        # Save frames based on the interval
        if frame_count % interval == 0:
            # Format timestamp as H:M:S
            timestamp = str(timedelta(seconds=frame_count / fps)).split(".")[0]
            # Include video name in the file name
            frame_name = f"{video_name}_{timestamp.replace(':', '_')}-{saved_count:05d}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, frame)
            # print(f"Saved frame: {frame_path}")
            saved_count += 1

        frame_count += 1

    capture.release()
    print(f"Finished extracting from {video_path}, total saved: {saved_count} frames.")


def process_videos(input_folder, output_folder, frame_rate=1):
    """
    Process all videos in the input folder and its subdirectories.

    :param input_folder: Path to the folder containing videos
    :param output_folder: Path to the folder where extracted frames will be saved
    :param frame_rate: Number of frames to extract per second
    """
    # Define supported video extensions
    supported_extensions = (".mp4", ".avi", ".mkv", ".mov", ".flv")

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(supported_extensions):  # Check if file is a video
                video_path = os.path.join(root, file)
                video_name = os.path.splitext(file)[0]  # Get video name without extension

                # Create output folder for each video
                relative_path = os.path.relpath(root, input_folder)  # Maintain subfolder structure
                video_output_folder = os.path.join(output_folder, relative_path, video_name)

                # Ensure the output folder exists
                os.makedirs(video_output_folder, exist_ok=True)

                print(f"Processing video: {video_path}")
                try:
                    extract_frames(video_path, video_output_folder, frame_rate)
                except Exception as e:
                    print(f"Failed to process video {video_path}: {e}")

