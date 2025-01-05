import os
import subprocess

# Update the paths accordingly
image_folder = "generated_images"
music_path = "msc2.mp3"
output_video = "output_video1.mp4"

def create_video_ffmpeg(image_folder, music_path, output_video):
    """Creates a video using FFmpeg with the given images and music."""
    ffmpeg_cmd = [
        r"C:\ffmpeg\bin\ffmpeg.exe",  # Use raw string to handle backslashes
        "-y",  # Overwrite output files without asking
        "-r", "24",  # Frame rate
        "-i", f"{image_folder}/frame_%d.png",  # Input images
        "-i", music_path,  # Input music
        "-c:v", "libx264",  # Video codec
        "-pix_fmt", "yuv420p",  # Pixel format for compatibility
        "-c:a", "aac",  # Audio codec
        "-shortest",  # End video when the shortest stream ends
        output_video
    ]
    subprocess.run(ffmpeg_cmd, check=True)


def main():
    if not os.path.exists(image_folder):
        print(f"Image folder '{image_folder}' does not exist. Please generate images first.")
        return

    print("Analyzing music...")
    tempo = 120  # Default tempo value or replace with your analysis logic
    print(f"Detected tempo: {tempo} BPM")
    
    print("Creating video using FFmpeg...")
    create_video_ffmpeg(image_folder, music_path, output_video)
    print(f"Video created successfully: {output_video}")

if __name__ == "__main__":
    main()
