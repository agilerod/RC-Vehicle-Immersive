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
JETSON_IP = '192.168.68.110'
CONTROL_PORT = 5005

# Inicializar conexión TCP a Jetson
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((JETSON_IP, CONTROL_PORT))

# Inicializar pygame y joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Loop principal rápido
def capture_and_send():
    while True:
        pygame.event.pump()

        steering_axis = joystick.get_axis(0)
        accel_axis = joystick.get_axis(2)
        brake_axis = joystick.get_axis(3)
        clutch_axis = joystick.get_axis(1)
        boton_freno_mano = joystick.get_button(5)

        angulo_servo = int((steering_axis + 1) * 90)     # 0 a 180
        acelerador = int((1 - accel_axis) * 100)         # 0 a 100
        freno = int((1 - brake_axis) * 100)              # 0 a 100

        # Formato de mensaje
        message = f"{angulo_servo},{acelerador},{freno},{boton_freno_mano}\n"
        try:
            sock.sendall(message.encode())
        except BrokenPipeError:
            print("Conexión con Jetson perdida")
            break

        time.sleep(0.01)  # Latencia mínima aceptable (ajustable)

def main():
    """Main entry point."""
    try:
        capture_and_send()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 