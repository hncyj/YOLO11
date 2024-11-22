from custom.utils.extract_frame import process_videos

if __name__ == "__main__":
    input_folder = "/home/chenyinjie/superaccurate/files/videos/videos20241122"  
    output_folder = "/home/chenyinjie/superaccurate/files/photos/videos20241122"  
    frame_rate = 5  # intervals = int(fps // frame_rate)
    process_videos(input_folder, output_folder, frame_rate)