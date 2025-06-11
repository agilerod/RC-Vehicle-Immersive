# Hardware Connections

## Overview
This document describes the hardware connections and specifications for the RC Vehicle Immersive project.

## Components

### Jetson Nano Developer Kit
- Model: NVIDIA Jetson Nano Developer Kit
- OS: JetPack 4.6+
- RAM: 4GB
- Storage: 32GB eMMC

### Camera
- Model: Raspberry Pi Camera Module v2
- Interface: CSI-2
- Resolution: 1080p30
- Connection: CSI connector on Jetson Nano

### Arduino Nano ESP32
- Model: Arduino Nano ESP32
- CPU: ESP32-S3
- RAM: 512KB
- Flash: 4MB
- Connection: UART to Jetson Nano
- Features:
  - WiFi connectivity
  - OTA updates
  - Servo control
  - Status LED

#### Arduino Dependencies
- **Libraries Required**:
  - ESP32Servo (v0.13.0)
    - Purpose: Control de servos en ESP32
    - URL: https://github.com/madhephaestus/ESP32Servo
  - ArduinoOTA (v1.0.0)
    - Purpose: Actualizaciones Over-The-Air
    - URL: https://github.com/arduino-libraries/ArduinoOTA
  - ArduinoJson (v6.21.3)
    - Purpose: Manejo de JSON para configuración
    - URL: https://github.com/bblanchon/ArduinoJson

- **Development Environment**:
  - Arduino IDE 2.0+ o PlatformIO
  - ESP32 Board Support Package
  - USB-C cable para programación

- **Configuration**:
  - Velocidad de monitor serie: 115200 baud
  - Puerto USB: CDC (Serial)
  - Debug level: 5 (verbose)

### Motor Control
- ESC: Hobbywing QuicRun 1060
- Servo: Standard RC servo (e.g., TowerPro SG90)
- Power: 2S LiPo battery (7.4V)

### Joystick
- Model: Logitech G29
- Interface: USB
- Connected to: Laptop

## Pin Connections

### Jetson Nano to Arduino
| Jetson Nano | Arduino Nano ESP32 | Description |
|-------------|-------------------|-------------|
| UART_TX (8) | RX (GPIO18)       | UART TX     |
| UART_RX (10)| TX (GPIO17)       | UART RX     |
| GND         | GND               | Ground      |

### Arduino to Motor Control
| Arduino Nano ESP32 | ESC/Servo | Description |
|-------------------|-----------|-------------|
| GPIO13            | Servo     | Steering    |
| GPIO2             | LED       | Status LED  |
| 5V                | Servo     | Power       |
| GND               | Servo     | Ground      |

### Camera to Jetson
- CSI connector on Jetson Nano
- Camera ribbon cable to CSI port

## Power Requirements

### Jetson Nano
- Input: 5V/4A
- Power Supply: Official Jetson Nano power supply

### Arduino Nano ESP32
- Input: 5V from USB or external supply
- Current: ~100mA
- WiFi power consumption: ~100mA when active
- Servo power: 5V from external supply

### Motor Control
- ESC Input: 2S LiPo (7.4V)
- Servo: 5V from ESC BEC

## Network Configuration

### Jetson Nano
- Static IP: 192.168.68.101
- Subnet: 255.255.255.0
- Gateway: 192.168.68.1

### Laptop
- IP: 192.168.68.100
- Subnet: 255.255.255.0
- Gateway: 192.168.68.1

### Arduino Nano ESP32
- WiFi enabled
- OTA updates supported
- Static IP configuration available
- WiFi power management enabled

## Ports Used
- UDP Control: 5005
- Video Stream: 5000
- UART: 115200 baud
- OTA: 3232 (default)

## Safety Considerations
1. Always disconnect battery before making connections
2. Double-check polarity of all connections
3. Ensure proper voltage levels for each component
4. Use appropriate wire gauge for power connections
5. Secure all connections to prevent vibration damage
6. Test all components individually before full integration
7. Keep WiFi credentials secure and use strong passwords
8. Regularly update firmware via OTA

## Troubleshooting

### Camera Issues
1. If camera not detected:
   - Check CSI cable connection
   - Verify camera is enabled in Jetson config
   - Check camera power LED

### Arduino Issues
1. If Arduino not communicating:
   - Verify UART connections
   - Check baud rate settings
   - Test with serial monitor
   - Check WiFi connection status
   - Verify OTA functionality
   - Check library versions match requirements
   - Verify ESP32 board support is installed

### Motor Control Issues
1. If motor control not responding:
   - Check ESC power connection
   - Verify servo signal wire
   - Test ESC calibration
   - Check servo pulse width settings
   - Verify servo library initialization

### Network Issues
1. If network issues:
   - Verify IP configurations
   - Check WiFi connection
   - Test with ping
   - Verify OTA connectivity
   - Check WiFi signal strength
   - Verify WiFi credentials in config.h

## Configuration Files
- Arduino configuration is stored in `config.h` (not in repository)
- WiFi credentials should be kept secure
- OTA password should be strong and unique
- Servo calibration values should be verified for your specific hardware
- PlatformIO configuration in `platformio.ini`

## Development Setup

### Arduino IDE Setup
1. Install Arduino IDE 2.0 or later
2. Add ESP32 board support:
   - Add URL: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   - Install "ESP32" board package
3. Install required libraries:
   - ESP32Servo
   - ArduinoOTA
   - ArduinoJson

### PlatformIO Setup
1. Install PlatformIO IDE
2. Clone repository
3. Open project folder
4. PlatformIO will automatically install dependencies

### First Time Setup
1. Connect Arduino Nano ESP32 via USB
2. Select correct board in IDE
3. Select correct port
4. Upload code
5. Monitor serial output at 115200 baud
6. Verify WiFi connection
7. Test OTA functionality 