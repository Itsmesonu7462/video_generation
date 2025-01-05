import librosa
import numpy as np
import matplotlib.pyplot as plt
from moviepy import ImageSequenceClip

# Load audio file
audio_path = "msc2.mp3"
y, sr = librosa.load(audio_path, sr=None)

# Extract features
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Generate visuals for beats
frames = []
for beat_time in beat_times:
    plt.figure(figsize=(6, 6))
    plt.axis('off')
    plt.title(f"Beat at {beat_time:.2f}s", fontsize=8)
    plt.pie(np.random.rand(10), colors=plt.cm.viridis(np.random.rand(10)))
    plt.savefig(f"frame_{int(beat_time * 100)}.png", bbox_inches='tight')
    frames.append(f"frame_{int(beat_time * 100)}.png")
    plt.close()

# Assemble frames into video
clip = ImageSequenceClip(frames, fps=30)
clip.write_videofile("output_video.mp4", codec="libx264")
