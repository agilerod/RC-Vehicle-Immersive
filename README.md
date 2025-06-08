# 🚗 RC Vehicle Immersive Control System

Este proyecto busca crear una experiencia inmersiva de conducción para un auto RC, integrando Jetson Nano, Arduino Nano ESP32, y un visor VR (Oculus/Meta Quest), con control mediante un volante Logitech G29 o similar.

---

## 🎯 Objetivo

Desarrollar un sistema de control de bajo costo y baja latencia que permita:

- Transmitir video en tiempo real desde el auto (Jetson Nano + cámara)
- Controlar motores vía ESP32 mediante comandos UART desde Jetson
- Visualizar la conducción con una experiencia inmersiva usando VR
- Integrar joystick de conducción real (volante + pedales) al sistema

---

## 🧩 Componentes del sistema

| Componente        | Descripción                                      |
|-------------------|--------------------------------------------------|
| Jetson Nano       | Procesamiento de video y comunicación UART       |
| ESP32 Nano        | Control de motores, servidor web de estado       |
| Cámara            | Cámara global shutter o RPi v2 para Jetson       |
| Oculus/VR Headset | Visualización inmersiva (proyecto Unity opcional)|
| Joystick G29      | Input del usuario (aceleración, dirección)       |

---

## 🗂️ Estructura del repositorio

- `hardware/`: Esquemáticos, diagramas, detalles de conexión
- `firmware/`: Código cargado en ESP32 para control de motor y UI web
- `jetson/`: Scripts en Python/C++ para control, video, joystick
- `unity-vr-interface/`: Proyecto Unity para visualización en VR (opcional)
- `docs/`: Diagramas, arquitectura, documentación complementaria

---

## 🚀 Cómo comenzar

### Requisitos mínimos

- Jetson Nano con JetPack 4.6+
- Arduino Nano ESP32 (UART activo en GPIO18)
- Cámara compatible V4L2
- Control Logitech G29 u otro joystick
- Conexión WiFi compartida entre Jetson y ESP32

### 1. Clona el proyecto

```bash
git clone https://github.com/tuusuario/RC-Vehicle-Immersive.git
cd RC-Vehicle-Immersive
