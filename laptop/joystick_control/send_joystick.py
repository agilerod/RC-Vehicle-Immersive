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
import os
from typing import Dict, Any

# Configuración por defecto
DEFAULT_CONFIG = {
    'jetson_ip': '192.168.68.110',
    'jetson_port': 5005,
    'update_rate': 0.01  # 100Hz
}

def load_config() -> Dict[str, Any]:
    """Carga la configuración desde un archivo o usa valores por defecto."""
    config = DEFAULT_CONFIG.copy()
    
    # Intentar cargar desde archivo de configuración
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                file_config = json.load(f)
                config.update(file_config)
        except Exception as e:
            print(f"Error cargando configuración: {e}")
            print("Usando configuración por defecto")
    
    return config

def create_tcp_connection(ip: str, port: int) -> socket.socket:
    """Crea una conexión TCP con el Jetson."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        print(f"Conectado a Jetson en {ip}:{port}")
        return sock
    except Exception as e:
        print(f"Error conectando a Jetson: {e}")
        sys.exit(1)

def init_joystick() -> pygame.joystick.Joystick:
    """Inicializa el joystick y retorna el objeto."""
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("No se detectó ningún joystick")
        sys.exit(1)
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detectado: {joystick.get_name()}")
    return joystick

def capture_and_send(joystick: pygame.joystick.Joystick, sock: socket.socket, config: Dict[str, Any]):
    """Captura datos del joystick y los envía al Jetson."""
    print("Iniciando captura de datos del joystick...")
    print("Presiona Ctrl+C para detener")
    
    try:
        while True:
            pygame.event.pump()
            
            # Capturar datos del joystick
            steering = int(joystick.get_axis(0) * 90 + 90)  # Eje X: 0-180
            clutch = int((joystick.get_axis(1) + 1) * 50)   # Eje Y: 0-100
            throttle = int((joystick.get_axis(2) + 1) * 50) # Eje Z: 0-100
            brake = int((joystick.get_axis(3) + 1) * 50)    # Eje R: 0-100
            handbrake = 1 if joystick.get_button(5) else 0  # Botón 5
            
            # Crear mensaje
            message = {
                'steering': steering,
                'clutch': clutch,
                'throttle': throttle,
                'brake': brake,
                'handbrake': handbrake
            }
            
            # Enviar datos
            try:
                sock.sendall(json.dumps(message).encode() + b'\n')
            except Exception as e:
                print(f"Error enviando datos: {e}")
                break
            
            time.sleep(config['update_rate'])
            
    except KeyboardInterrupt:
        print("\nDeteniendo captura...")
    finally:
        sock.close()
        pygame.quit()

def main():
    """Main entry point."""
    try:
        # Cargar configuración
        config = load_config()
        
        # Crear conexión TCP
        sock = create_tcp_connection(config['jetson_ip'], config['jetson_port'])
        
        # Inicializar joystick
        joystick = init_joystick()
        
        # Iniciar captura y envío
        capture_and_send(joystick, sock, config)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 