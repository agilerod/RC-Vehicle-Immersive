#!/usr/bin/env python3
"""
Joystick control module for RC Vehicle Immersive project.
Handles reading from Logitech G29 and sending control signals via UDP.
"""

import pygame
import socket
import time
import json
import logging
from pathlib import Path
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('joystick_control.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class JoystickController:
    def __init__(self, config_path='config.json'):
        self.config = self._load_config(config_path)
        self.setup_joystick()
        self.setup_network()
        
    def _load_config(self, config_path):
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default configuration
            config = {
                'jetson_ip': '192.168.68.101',
                'jetson_port': 5005,
                'update_rate': 20,  # Hz
                'deadzone': 0.1,
                'steering_axis': 0,
                'throttle_axis': 1
            }
            # Save default config
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)
            return config

    def setup_joystick(self):
        """Initialize pygame and joystick."""
        try:
            pygame.init()
            pygame.joystick.init()
            
            if pygame.joystick.get_count() == 0:
                raise RuntimeError("No joystick found!")
            
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            logging.info(f"Joystick initialized: {self.joystick.get_name()}")
            
        except Exception as e:
            logging.error(f"Failed to initialize joystick: {e}")
            raise

    def setup_network(self):
        """Setup UDP socket for communication."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            logging.info(f"UDP socket created for {self.config['jetson_ip']}:{self.config['jetson_port']}")
        except Exception as e:
            logging.error(f"Failed to create UDP socket: {e}")
            raise

    def apply_deadzone(self, value):
        """Apply deadzone to joystick values."""
        if abs(value) < self.config['deadzone']:
            return 0
        return value

    def read_controls(self):
        """Read and process joystick inputs."""
        pygame.event.pump()
        
        # Read raw values
        steering = self.joystick.get_axis(self.config['steering_axis'])
        throttle = self.joystick.get_axis(self.config['throttle_axis'])
        
        # Apply deadzone
        steering = self.apply_deadzone(steering)
        throttle = self.apply_deadzone(throttle)
        
        # Scale to -100 to 100
        steering = int(steering * 100)
        throttle = int(-throttle * 100)  # Invert throttle axis
        
        return steering, throttle

    def send_controls(self, steering, throttle):
        """Send control values via UDP."""
        try:
            message = f"{steering},{throttle}\n"
            self.sock.sendto(message.encode(), 
                           (self.config['jetson_ip'], self.config['jetson_port']))
            logging.debug(f"Sent: {message.strip()}")
        except Exception as e:
            logging.error(f"Failed to send controls: {e}")

    def run(self):
        """Main control loop."""
        logging.info("Starting joystick control loop...")
        try:
            while True:
                steering, throttle = self.read_controls()
                self.send_controls(steering, throttle)
                time.sleep(1.0 / self.config['update_rate'])
                
        except KeyboardInterrupt:
            logging.info("Control loop terminated by user")
        except Exception as e:
            logging.error(f"Control loop error: {e}")
        finally:
            pygame.quit()
            self.sock.close()

if __name__ == "__main__":
    try:
        controller = JoystickController()
        controller.run()
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)
