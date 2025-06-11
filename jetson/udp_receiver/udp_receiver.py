#!/usr/bin/env python3
"""
UDP receiver module for RC Vehicle Immersive project.
Receives control signals from laptop and forwards them to Arduino.
"""

import socket
import json
import logging
import sys
import serial
import time
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('udp_receiver.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class UDPReceiver:
    def __init__(self, config_path='config.json'):
        self.config = self._load_config(config_path)
        self.setup_network()
        self.setup_serial()
        
    def _load_config(self, config_path):
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default configuration
            config = {
                'udp_port': 5005,
                'serial_port': '/dev/ttyUSB0',
                'baud_rate': 115200,
                'update_rate': 20,  # Hz
                'enable_serial': True
            }
            # Save default config
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=4)
            return config

    def setup_network(self):
        """Setup UDP socket for receiving control signals."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind(("0.0.0.0", self.config['udp_port']))
            logging.info(f"UDP socket bound to port {self.config['udp_port']}")
        except Exception as e:
            logging.error(f"Failed to setup UDP socket: {e}")
            raise

    def setup_serial(self):
        """Setup serial connection to Arduino."""
        if not self.config['enable_serial']:
            self.serial = None
            return

        try:
            self.serial = serial.Serial(
                port=self.config['serial_port'],
                baudrate=self.config['baud_rate'],
                timeout=1
            )
            logging.info(f"Serial connection established on {self.config['serial_port']}")
        except Exception as e:
            logging.error(f"Failed to setup serial connection: {e}")
            self.serial = None

    def process_controls(self, data):
        """Process received control data."""
        try:
            steering, throttle = map(int, data.decode().strip().split(","))
            logging.debug(f"Received - Steering: {steering}, Throttle: {throttle}")
            return steering, throttle
        except Exception as e:
            logging.error(f"Failed to process control data: {e}")
            return None, None

    def send_to_arduino(self, steering, throttle):
        """Send control values to Arduino."""
        if not self.serial:
            return

        try:
            message = f"S{steering}T{throttle}\n"
            self.serial.write(message.encode())
            logging.debug(f"Sent to Arduino: {message.strip()}")
        except Exception as e:
            logging.error(f"Failed to send to Arduino: {e}")

    def run(self):
        """Main receiver loop."""
        logging.info("Starting UDP receiver loop...")
        try:
            while True:
                data, addr = self.sock.recvfrom(1024)
                logging.debug(f"Received data from {addr}")
                
                steering, throttle = self.process_controls(data)
                if steering is not None and throttle is not None:
                    self.send_to_arduino(steering, throttle)
                
                time.sleep(1.0 / self.config['update_rate'])
                
        except KeyboardInterrupt:
            logging.info("Receiver loop terminated by user")
        except Exception as e:
            logging.error(f"Receiver loop error: {e}")
        finally:
            self.sock.close()
            if self.serial:
                self.serial.close()

if __name__ == "__main__":
    try:
        receiver = UDPReceiver()
        receiver.run()
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1) 