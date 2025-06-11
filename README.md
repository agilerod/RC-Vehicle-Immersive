# 🚗 RC Vehicle Immersive Control System

Este proyecto busca crear una experiencia inmersiva de conducción para un auto RC, integrando Jetson Nano, Arduino Nano ESP32, y un visor VR (Oculus/Meta Quest), con control mediante un volante Logitech G29 o similar.

## 🎯 Objetivo

Desarrollar un sistema de control de bajo costo y baja latencia que permita:

* Transmitir video en tiempo real desde el auto (Jetson Nano + cámara)
* Controlar motores vía ESP32 mediante comandos UART desde Jetson
* Visualizar la conducción con una experiencia inmersiva usando VR
* Integrar joystick de conducción real (volante + pedales) al sistema

## 🧩 Componentes del sistema

| Componente        | Descripción                                       |
| ----------------- | ------------------------------------------------- |
| Jetson Nano       | Procesamiento de video y comunicación UDP         |
| ESP32 Nano        | Control de motores, WiFi, OTA updates             |
| Cámara RPi v2     | Cámara para Jetson con streaming RTSP             |
| Joystick G29      | Input del usuario (aceleración, dirección)        |
| Laptop            | Visualización y control remoto                    |

## 🗂️ Estructura del repositorio

```
RC-Vehicle-Immersive/
├── docs/                    # Documentación del sistema
│   ├── architecture/        # Diagramas de arquitectura
│   ├── hardware/           # Especificaciones de hardware
│   └── startup_guide.md    # Guía de inicio paso a paso
├── firmware/               # Código para Arduino
│   └── motor_control/      # Control de motores ESP32
├── jetson/                 # Código para Jetson Nano
│   ├── udp_receiver/       # Receptor de comandos UDP
│   └── video_streaming/    # Streaming de video RTSP
├── laptop/                 # Código para laptop
│   ├── joystick_control/   # Control con G29
│   ├── video_viewer/       # Visor de video
│   └── requirements.txt    # Dependencias Python
├── hardware/              # Esquemáticos y conexiones
├── unity-vr-interface/    # Proyecto Unity (opcional)
└── tools/                 # Herramientas de desarrollo
```

## 🚀 Cómo comenzar

### Requisitos mínimos

* Jetson Nano con JetPack 4.6+
* Arduino Nano ESP32
* Cámara RPi v2
* Control Logitech G29
* Conexión WiFi compartida

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/agilerod/RC-Vehicle-Immersive.git
   cd RC-Vehicle-Immersive
   ```

2. Configura el Arduino:
   - Instala el firmware desde `firmware/motor_control/`
   - Configura las credenciales WiFi en `config.h`

3. Configura la Jetson:
   - Instala las dependencias necesarias
   - Configura la cámara CSI
   - Ajusta la IP en los scripts

4. Configura la laptop:
   - Instala las dependencias: `pip install -r laptop/requirements.txt`
   - Configura la IP de la Jetson en los scripts

### Uso

Consulta la [guía de inicio](docs/startup_guide.md) para instrucciones detalladas sobre cómo poner en funcionamiento el sistema.

## 🔧 Mantenimiento

* Verifica regularmente las conexiones
* Mantén el firmware actualizado
* Limpia la lente de la cámara
* Monitorea la temperatura de la Jetson

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviarnos pull requests.

## 📫 Contacto

Rodrigo Bermúdez - [@agilerod](https://github.com/agilerod)

Link del proyecto: [https://github.com/agilerod/RC-Vehicle-Immersive](https://github.com/agilerod/RC-Vehicle-Immersive)
