#!/usr/bin/env python3
"""
Video Streamer for RC Vehicle
This script captures video from the camera and streams it to the laptop.
"""

import cv2
import numpy as np
import socket
import time
import threading
from typing import Optional, Tuple

# Configuration
UDP_IP = "192.168.1.101"  # Laptop IP address
UDP_PORT = 8889
CAMERA_ID = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS = 30
JPEG_QUALITY = 80

class VideoStreamer:
    def __init__(self, ip: str, port: int, camera_id: int):
        """Initialize the video streamer."""
        self.ip = ip
        self.port = port
        self.camera_id = camera_id
        
        # Initialize UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Initialize camera
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera {camera_id}")
        
        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, FPS)
        
        # Control variables
        self.running = True
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.fps = 0
        
    def capture_frame(self) -> Optional[np.ndarray]:
        """Capture a frame from the camera."""
        ret, frame = self.cap.read()
        if not ret:
            print("Error capturing frame")
            return None
        return frame
    
    def encode_frame(self, frame: np.ndarray) -> Optional[bytes]:
        """Encode frame as JPEG."""
        try:
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY]
            _, buffer = cv2.imencode('.jpg', frame, encode_param)
            return buffer.tobytes()
        except Exception as e:
            print(f"Error encoding frame: {e}")
            return None
    
    def stream_frame(self, frame_data: bytes) -> None:
        """Send frame data over UDP."""
        try:
            self.sock.sendto(frame_data, (self.ip, self.port))
        except Exception as e:
            print(f"Error sending frame: {e}")
    
    def run(self) -> None:
        """Start the video streamer."""
        print(f"Starting video stream to {self.ip}:{self.port}")
        print("Press Ctrl+C to stop")
        
        try:
            while self.running:
                # Capture frame
                frame = self.capture_frame()
                if frame is None:
                    continue
                
                # Add FPS counter
                self.frame_count += 1
                current_time = time.time()
                if current_time - self.last_fps_time >= 1.0:
                    self.fps = self.frame_count
                    self.frame_count = 0
                    self.last_fps_time = current_time
                
                cv2.putText(
                    frame,
                    f"FPS: {self.fps}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )
                
                # Encode and stream frame
                frame_data = self.encode_frame(frame)
                if frame_data is not None:
                    self.stream_frame(frame_data)
                
                # Control frame rate
                time.sleep(1.0 / FPS)
                
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            self.running = False
            self.cap.release()
            self.sock.close()

def main():
    """Main entry point."""
    try:
        streamer = VideoStreamer(UDP_IP, UDP_PORT, CAMERA_ID)
        streamer.run()
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 