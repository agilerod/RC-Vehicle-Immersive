# Motor Control Firmware

This directory contains the firmware for the Arduino Nano ESP32 that controls the RC vehicle's steering servo.

## Hardware Requirements

- Arduino Nano ESP32
- Steering servo (compatible with 5V)
- LED indicator
- Power supply (5V)
- USB-C cable for programming

## Software Requirements

- Arduino IDE 2.0+ or PlatformIO
- ESP32 Board Support Package
- Required libraries:
  - ESP32Servo (v0.13.0)
  - ArduinoOTA (v1.0.0)
  - ArduinoJson (v6.21.3)

## Setup Instructions

### Using Arduino IDE

1. Install Arduino IDE 2.0 or later
2. Add ESP32 board support:
   - Open Preferences
   - Add `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json` to Additional Board Manager URLs
   - Install "ESP32" from Board Manager
3. Install required libraries from Library Manager
4. Open `motor_control.ino`
5. Configure WiFi credentials in `config.h`
6. Select "Arduino Nano ESP32" from board menu
7. Upload the sketch

### Using PlatformIO

1. Install PlatformIO IDE or VS Code extension
2. Open the project directory
3. Configure WiFi credentials in `config.h`
4. Build and upload using PlatformIO

## Usage

The firmware accepts the following commands via serial:

- `S<angle>`: Set steering angle (0-180)
- `C`: Center steering (90 degrees)
- `T`: Run sweep test

Example:
```
S45    # Set steering to 45 degrees
C      # Center steering
T      # Run sweep test
```

## OTA Updates

The firmware supports Over-The-Air updates:

1. Connect to the same WiFi network as the Arduino
2. Use Arduino IDE or PlatformIO to upload over WiFi
3. The device will appear as "rc-vehicle" in the port selection

## Troubleshooting

1. **Servo not responding**
   - Check power supply
   - Verify servo connections
   - Check serial monitor for error messages

2. **WiFi connection issues**
   - Verify WiFi credentials
   - Check signal strength
   - Ensure 2.4GHz network

3. **OTA update fails**
   - Check WiFi connection
   - Verify device is on same network
   - Check available flash space

## Development

### Flow Control

1. Serial commands are processed in the main loop
2. OTA updates are handled in the background
3. LED indicates system status:
   - Solid ON: WiFi connected
   - Blinking: OTA update in progress
   - OFF: Error or disconnected

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 