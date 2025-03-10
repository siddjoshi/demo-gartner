# Real-Time Music Visualizer

A Python application that captures real-time audio input from your microphone and creates a live waveform visualization.

## Features
- Real-time audio input capture using PyAudio
- Live waveform visualization using Matplotlib
- Dynamic updating display

## Requirements
- Python 3.7+
- Virtual Environment
- Required packages listed in requirements.txt

## Setup Instructions
1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Ensure your microphone is connected and working
2. Run the program:
```bash
python visualizer.py
```

3. Speak or play music to see the audio visualization
4. Press Ctrl+C to exit

## Technical Details
- Uses PyAudio for audio capture
- Matplotlib for real-time visualization
- Numpy for audio data processing