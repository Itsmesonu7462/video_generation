const express = require('express');
const fs = require('fs');
const { exec } = require('child_process');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json({ limit: '50mb' })); // Increase payload size for base64 frames

app.post('/generate-video', async (req, res) => {
  const frames = req.body.frames; // Base64 images
  const audioPath = 'uploaded_audio.mp3';

  // Save frames to disk
  frames.forEach((frame, index) => {
    const base64Data = frame.replace(/^data:image\/png;base64,/, "");
    fs.writeFileSync(`frames/frame_${index.toString().padStart(4, '0')}.png`, base64Data, 'base64');
  });

  // FFmpeg command to generate video
  exec(`ffmpeg -r 30 -i frames/frame_%04d.png -i ${audioPath} -c:v libx264 -c:a aac output.mp4`, (err) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error generating video');
      return;
    }
    res.download('output.mp4');
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
