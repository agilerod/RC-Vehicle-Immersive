# RC-Vehicle-Immersive

Sistema de conducción inmersiva para vehículo RC (Arrma Senton 3S) utilizando Jetson Nano Developer Kit.

## Descripción

Este proyecto implementa un sistema de control inmersivo para un vehículo RC, permitiendo:
- Control mediante joystick desde una laptop
- Transmisión de video en tiempo real desde la Jetson Nano
- Control de motores y servos mediante Arduino Nano ESP32
- Preparado para integración futura con VR (Oculus)

## Estructura del Proyecto

```
RC-Vehicle-Immersive/
├── laptop/                 # Código para la laptop controladora
│   ├── joystick_control/   # Control de joystick y transmisión UDP
│   └── video_viewer/       # Visualización de stream de video
├── jetson/                 # Código para la Jetson Nano
│   ├── udp_receiver/       # Recepción de comandos UDP
│   └── video_streaming/    # Transmisión de video
├── firmware/               # Código para Arduino Nano ESP32
│   └── motor_control/      # Control de motores y servos
├── unity-vr-interface/     # Futura integración con Unity y VR
├── docs/                   # Documentación y esquemas
│   ├── architecture/       # Diagramas de arquitectura
│   └── hardware/          # Especificaciones de hardware
└── hardware/              # Especificaciones de conexiones
```

## Requisitos de Hardware

- Jetson Nano Developer Kit
- Cámara Raspberry Pi v2
- Arduino Nano ESP32
- Joystick Logitech G29
- Vehículo RC Arrma Senton 3S
- Laptop con WiFi
- Oculus VR (futuro)

## Requisitos de Software

### Laptop
- Python 3.8+
- Pygame
- VLC o similar para visualización de video

### Jetson Nano
- JetPack 4.6+
- GStreamer
- Python 3.8+

### Arduino
- Arduino IDE
- ESP32 Board Support

## Configuración

1. Configurar red WiFi entre Jetson y laptop
2. Instalar dependencias en cada dispositivo
3. Configurar direcciones IP en los scripts
4. Conectar hardware según diagramas en docs/hardware

## Uso

1. Iniciar transmisión de video en Jetson:
   ```bash
   cd jetson/video_streaming
   ./stream_camera.sh
   ```

2. Iniciar control de joystick en laptop:
   ```bash
   cd laptop/joystick_control
   python send_joystick.py
   ```

3. Iniciar receptor UDP en Jetson:
   ```bash
   cd jetson/udp_receiver
   python udp_receiver.py
   ```

## Contribución

1. Fork el repositorio
2. Crear rama para feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
