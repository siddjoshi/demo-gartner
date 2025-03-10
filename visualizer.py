import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

## Class deninition
class AudioVisualizer:
    def __init__(self):
        # Audio settings
        self.CHUNK = 1024 * 2
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        
        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=False,
            frames_per_buffer=self.CHUNK
        )
        
        # Initialize the plot
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-', lw=2)
        self.ax.set_title('Real-Time Audio Waveform')
        self.ax.set_xlabel('Sample')
        self.ax.set_ylabel('Amplitude')
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlim(0, self.CHUNK)
        self.ax.grid(True)
        
    def update_plot(self, frame):
        try:
            data = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.float32)
            self.line.set_data(range(len(data)), data)
            return self.line,
        except Exception as e:
            print(f"Error: {e}")
            return self.line,
    
    def run(self):
        ani = FuncAnimation(
            self.fig, 
            self.update_plot, 
            interval=30,
            blit=True
        )
        plt.show()
    
    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    try:
        visualizer.run()
    except KeyboardInterrupt:
        print("\nStopping the visualizer...")
    finally:
        visualizer.cleanup()
