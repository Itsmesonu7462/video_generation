# video_generation
# Video Generation Project

## Overview
This project is designed to generate videos from user-provided text prompts and music files. It utilizes a text-to-image model (Stable Diffusion) to create a sequence of images based on a given prompt and combines them with a provided audio track to produce a cohesive video.

---

## Features
1. **Text-to-Image Generation:** Uses the Stable Diffusion model to generate images based on text prompts.
2. **Audio Integration:** Adds user-provided music to the generated video.
3. **Customizable Settings:** Users can specify the number of frames, resolution, and duration.

---

## Requirements
### Hardware
- **No NVIDIA GPU required** (Runs on CPU).
  - Note: Running on CPU will be slower compared to GPU processing.

### Software
- Python 3.9 or higher
- Libraries:
  - `diffusers`
  - `torch`
  - `transformers`
  - `PIL` (Pillow)
  - `moviepy`
  - `numpy`
- Stable Diffusion Model: `CompVis/stable-diffusion-v1-4`

---

## Installation
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python libraries:
    ```bash
    pip install diffusers torch transformers pillow moviepy numpy
    ```

3. Download the Stable Diffusion model files using `diffusers`. The files will be cached automatically.

---

## Usage
1. Create a Python script `vid_gen.py` with the following core functionality:

    ### Key Functions:
    - **Generate Images**
      ```python
      from diffusers import StableDiffusionPipeline
      from PIL import Image

      def generate_images(prompt, num_images=10):
          pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
          pipeline.to("cpu")  # Use CPU
          images = []
          for _ in range(num_images):
              images.append(pipeline(prompt).images[0])
          return images
      ```

    - **Combine Images and Audio**
      ```python
      from moviepy.editor import ImageSequenceClip, AudioFileClip

      def create_video(images, audio_path, output_path="output.mp4", fps=10):
          image_sequence = [Image.fromarray((np.array(img)).astype("uint8")) for img in images]
          clip = ImageSequenceClip([np.array(img) for img in image_sequence], fps=fps)
          audio = AudioFileClip(audio_path)
          clip = clip.set_audio(audio)
          clip.write_videofile(output_path, codec="libx264")
      ```

2. Run the script:
    ```bash
    python vid_gen.py
    ```

### Example Input
- Prompt: `"A serene sunset over a mountain range with vibrant colors."`
- Music: `"background_music.mp3"`

### Example Output
- A video file named `output.mp4` with the generated frames and background music.

---

## Performance Notes
- **Running on CPU:** Processing may take longer. Optimize prompts and reduce the number of frames for faster results.
- **Image Quality:** The quality depends on the text prompt and model settings.

---

## Troubleshooting
### Common Errors
1. **Torch not compiled with CUDA enabled:**
   - Ensure the `pipeline.to("cpu")` line is present to avoid GPU-related issues.

2. **Missing model files:**
   - Check the Stable Diffusion model is downloaded properly in the `~/.cache/huggingface` directory.

3. **Slow Processing:**
   - Use fewer frames or lower resolutions for faster processing.

---

## Future Improvements
1. Add support for custom resolutions and frame rates.
2. Optimize processing using multi-threading for CPU.
3. Explore integration with cloud GPU services for faster execution.

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute the code.

---

## Acknowledgments
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [Pillow](https://python-pillow.org/)

