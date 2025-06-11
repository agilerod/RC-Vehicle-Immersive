#!/usr/bin/env python3
"""
UDP Receiver for RC Vehicle
This script receives steering commands from the laptop and forwards them to the Arduino.
"""

import socket
import json
import time
import threading
import serial
from typing import Optional, Dict, Any

# Configuration
UDP_IP = "0.0.0.0"  # Listen on all interfaces
UDP_PORT = 8888
ARDUINO_PORT = "/dev/ttyUSB0"  # Update with actual port
ARDUINO_BAUD = 115200

class CommandReceiver:
    def __init__(self, udp_ip: str, udp_port: int, arduino_port: str, arduino_baud: int):
        """Initialize the command receiver."""
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.arduino_port = arduino_port
        self.arduino_baud = arduino_baud
        
        # Initialize UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((udp_ip, udp_port))
        
        # Initialize serial connection
        try:
            self.serial = serial.Serial(arduino_port, arduino_baud, timeout=1)
            print(f"Connected to Arduino on {arduino_port}")
        except Exception as e:
            print(f"Error connecting to Arduino: {e}")
            raise
        
        # Control variables
        self.running = True
        self.last_command: Optional[Dict[str, Any]] = None
        self.command_lock = threading.Lock()
        
    def receive_commands(self) -> None:
        """Receive UDP commands from laptop."""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                command = json.loads(data.decode())
                
                with self.command_lock:
                    self.last_command = command
                    print(f"Received command: {command}")
                    
            except Exception as e:
                print(f"Error receiving command: {e}")
                time.sleep(0.1)
    
    def process_commands(self) -> None:
        """Process received commands and send to Arduino."""
        while self.running:
            with self.command_lock:
                if self.last_command is not None:
                    try:
                        # Extract angle from command
                        angle = self.last_command.get("angle", 90)
                        
                        # Send command to Arduino
                        command = f"S{angle}\n"
                        self.serial.write(command.encode())
                        print(f"Sent to Arduino: {command.strip()}")
                        
                        # Clear last command
                        self.last_command = None
                        
                    except Exception as e:
                        print(f"Error processing command: {e}")
            
            time.sleep(0.05)  # 20Hz update rate
    
    def run(self) -> None:
        """Start the command receiver."""
        print(f"Starting UDP receiver on {self.udp_ip}:{self.udp_port}")
        
        # Start receiver thread
        receiver_thread = threading.Thread(target=self.receive_commands)
        receiver_thread.daemon = True
        receiver_thread.start()
        
        try:
            # Main processing loop
            self.process_commands()
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            self.running = False
            self.sock.close()
            self.serial.close()

def main():
    """Main entry point."""
    try:
        receiver = CommandReceiver(UDP_IP, UDP_PORT, ARDUINO_PORT, ARDUINO_BAUD)
        receiver.run()
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 