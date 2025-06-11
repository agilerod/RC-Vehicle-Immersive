#!/usr/bin/env python3
"""
Video stream viewer for RC Vehicle Immersive project.
Receives and displays video stream from Jetson Nano.
"""

import cv2
import numpy as np
import json
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('video_viewer.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class VideoViewer:
    def __init__(self, config_path='config.json'):
        self.config = self._load_config(config_path)
        self.setup_camera()
        
    def _load_config(self, config_path):
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default configuration
            config = {
                'jetson_ip': '192.168.68.101',
                'video_port': 5000,
                'window_name': 'RC Vehicle Stream',
                'frame_width': 640,
                'frame_height': 480,
                'fps': 30
            }
            # Save default config
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)
            return config

    def setup_camera(self):
        """Setup video capture from Jetson stream."""
        try:
            # RTSP URL for the stream
            rtsp_url = f"rtsp://{self.config['jetson_ip']}:{self.config['video_port']}"
            self.cap = cv2.VideoCapture(rtsp_url)
            
            if not self.cap.isOpened():
                raise RuntimeError("Failed to open video stream")
                
            logging.info(f"Video stream opened from {rtsp_url}")
            
        except Exception as e:
            logging.error(f"Failed to setup video capture: {e}")
            raise

    def process_frame(self, frame):
        """Process video frame (add overlays, etc)."""
        # Add timestamp
        timestamp = cv2.getTickCount() / cv2.getTickFrequency()
        cv2.putText(frame, f"Time: {timestamp:.2f}s", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return frame

    def run(self):
        """Main video viewing loop."""
        logging.info("Starting video viewer...")
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    logging.error("Failed to read frame")
                    break
                
                # Process frame
                frame = self.process_frame(frame)
                
                # Display frame
                cv2.imshow(self.config['window_name'], frame)
                
                # Check for exit key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
        except KeyboardInterrupt:
            logging.info("Video viewer terminated by user")
        except Exception as e:
            logging.error(f"Video viewer error: {e}")
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        viewer = VideoViewer()
        viewer.run()
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1) 