import os
from diffusers import StableDiffusionPipeline
import librosa
import subprocess

# Step 1: Generate Images from Prompt
def generate_images(prompt, output_dir="generated_images", num_images=5):
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading Stable Diffusion model...")
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    pipeline.to("cpu")  # Use GPU if available

    print(f"Generating {num_images} images for the prompt: {prompt}")
    images = []
    for i in range(num_images):
        image = pipeline(prompt).images[0]
        file_path = os.path.join(output_dir, f"frame_{i+1}.png")
        image.save(file_path)
        images.append(file_path)

    return images

# Step 2: Analyze Music
def analyze_music(music_path):
    print("Analyzing music...")
    y, sr = librosa.load(music_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    print(f"Detected tempo: {tempo} BPM")
    return tempo

# Step 3: Create Video Using FFmpeg
def create_video_ffmpeg(image_dir, music_path, output_video="output_video.mp4"):
    print("Creating video using FFmpeg...")

    # Create a text file with image filenames for FFmpeg
    images_txt = os.path.join(image_dir, "images.txt")
    with open(images_txt, "w") as f:
        for file_name in sorted(os.listdir(image_dir)):
            if file_name.endswith(".png"):
                f.write(f"file '{os.path.join(image_dir, file_name)}'\n")
                f.write("duration 1\n")  # 1-second duration per frame

  
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
    subprocess.run(ffmpeg_cmd)
    print(f"Video saved as {output_video}")

# Main Function
def main():
    # Inputs
    prompt = "A futuristic cityscape at night"
    music_path = "msc2.mp3"
    output_video = "output_video1.mp4"
    num_images = 5

    # Step 1: Generate visuals
    images = generate_images(prompt, num_images=num_images)

    # Step 2: Analyze music
    analyze_music(music_path)

    # Step 3: Create video using FFmpeg
    create_video_ffmpeg("generated_images", music_path, output_video)

if __name__ == "__main__":
    main()
