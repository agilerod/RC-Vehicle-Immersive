#!/usr/bin/env python3
"""
Joystick Control Script for RC Vehicle
This script reads input from a joystick and sends steering commands to the Arduino.
"""

import socket
import json
import time
import pygame
import sys
from typing import Tuple, Optional

# Configuration
UDP_IP = "192.168.1.100"  # Arduino IP address
UDP_PORT = 8888
JOYSTICK_DEADZONE = 0.1
STEERING_SENSITIVITY = 1.0

class JoystickController:
    def __init__(self, ip: str, port: int):
        """Initialize the joystick controller."""
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Initialize pygame
        pygame.init()
        pygame.joystick.init()
        
        # Check for joystick
        if pygame.joystick.get_count() == 0:
            raise RuntimeError("No joystick found!")
        
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print(f"Initialized {self.joystick.get_name()}")
        
        # Control variables
        self.running = True
        self.last_angle = 90  # Center position
        
    def map_joystick_to_angle(self, x: float) -> int:
        """Map joystick X position to steering angle (0-180)."""
        # Apply deadzone
        if abs(x) < JOYSTICK_DEADZONE:
            return 90
            
        # Map -1 to 1 range to 0 to 180
        angle = 90 + (x * 90 * STEERING_SENSITIVITY)
        return max(0, min(180, int(angle)))
    
    def send_command(self, angle: int) -> None:
        """Send steering command to Arduino."""
        command = {
            "command": "steer",
            "angle": angle,
            "timestamp": int(time.time() * 1000)
        }
        try:
            self.sock.sendto(json.dumps(command).encode(), (self.ip, self.port))
        except Exception as e:
            print(f"Error sending command: {e}")
    
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # A button
                    self.send_command(90)  # Center
                elif event.button == 1:  # B button
                    self.running = False
    
    def run(self) -> None:
        """Main control loop."""
        print("Starting joystick control...")
        print("Press A to center steering")
        print("Press B to exit")
        
        try:
            while self.running:
                self.handle_events()
                
                # Get joystick position
                x = self.joystick.get_axis(0)  # Left stick X
                angle = self.map_joystick_to_angle(x)
                
                # Only send if angle changed
                if angle != self.last_angle:
                    self.send_command(angle)
                    self.last_angle = angle
                    print(f"Steering: {angle}°")
                
                time.sleep(0.05)  # 20Hz update rate
                
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            # Center steering before exit
            self.send_command(90)
            pygame.quit()
            self.sock.close()

def main():
    """Main entry point."""
    try:
        controller = JoystickController(UDP_IP, UDP_PORT)
        controller.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 