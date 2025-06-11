#!/usr/bin/env python3
"""
Video Stream Viewer for RC Vehicle
This script receives and displays the video stream from the Jetson.
"""

import cv2
import numpy as np
import socket
import struct
import threading
import time
from typing import Optional, Tuple

# Configuration
UDP_IP = "0.0.0.0"  # Listen on all interfaces
UDP_PORT = 8889
BUFFER_SIZE = 65536
WINDOW_NAME = "RC Vehicle Stream"

class VideoStreamViewer:
    def __init__(self, ip: str, port: int):
        """Initialize the video stream viewer."""
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        
        # Video stream variables
        self.frame = None
        self.frame_lock = threading.Lock()
        self.running = True
        
        # Performance monitoring
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.fps = 0
        
    def receive_frame(self) -> None:
        """Receive and decode video frames."""
        while self.running:
            try:
                # Receive frame data
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                
                # Decode frame
                frame_data = np.frombuffer(data, dtype=np.uint8)
                frame = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)
                
                if frame is not None:
                    with self.frame_lock:
                        self.frame = frame
                        self.frame_count += 1
                        
                        # Calculate FPS
                        current_time = time.time()
                        if current_time - self.last_fps_time >= 1.0:
                            self.fps = self.frame_count
                            self.frame_count = 0
                            self.last_fps_time = current_time
                            
            except Exception as e:
                print(f"Error receiving frame: {e}")
                time.sleep(0.1)
    
    def display_frame(self) -> None:
        """Display the received video frame."""
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
        
        while self.running:
            with self.frame_lock:
                if self.frame is not None:
                    # Add FPS counter
                    cv2.putText(
                        self.frame,
                        f"FPS: {self.fps}",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )
                    
                    # Display frame
                    cv2.imshow(WINDOW_NAME, self.frame)
            
            # Check for exit key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break
    
    def run(self) -> None:
        """Start the video stream viewer."""
        print(f"Starting video stream viewer on {self.ip}:{self.port}")
        print("Press 'q' to quit")
        
        # Start receiver thread
        receiver_thread = threading.Thread(target=self.receive_frame)
        receiver_thread.daemon = True
        receiver_thread.start()
        
        try:
            # Main display loop
            self.display_frame()
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            self.running = False
            cv2.destroyAllWindows()
            self.sock.close()

def main():
    """Main entry point."""
    try:
        viewer = VideoStreamViewer(UDP_IP, UDP_PORT)
        viewer.run()
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 