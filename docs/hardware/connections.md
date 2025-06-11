# Hardware Connections

This document details the hardware connections and pin configurations for the RC Vehicle Immersive project.

## Arduino Nano ESP32

### Features
- WiFi connectivity
- OTA updates
- Servo control
- Status LED

### Pin Connections

| Component | Pin | Description |
|-----------|-----|-------------|
| Steering Servo | GPIO13 | PWM output for servo control |
| Status LED | GPIO2 | System status indicator |

### Power Requirements
- Input Voltage: 5V
- Servo Power: 5V
- WiFi Power: ~100mA when active

### Network Configuration
- WiFi enabled
- OTA updates supported
- Static IP configuration available

### Ports Used
- UDP Control: 8888
- OTA Updates: 3232

## Safety Considerations

1. **Power Supply**
   - Use regulated 5V power supply
   - Ensure adequate current capacity
   - Protect against voltage spikes

2. **Servo Control**
   - Verify servo limits
   - Check for mechanical interference
   - Monitor temperature

3. **WiFi Security**
   - Use WPA2 encryption
   - Change default credentials
   - Monitor network traffic

## Troubleshooting

1. **Servo Issues**
   - Check power supply
   - Verify PWM signal
   - Test with sweep command

2. **WiFi Problems**
   - Check signal strength
   - Verify credentials
   - Monitor connection status

3. **OTA Update Issues**
   - Check network connectivity
   - Verify flash space
   - Monitor update progress

## Configuration Files

1. **config.h**
   - WiFi credentials
   - Pin definitions
   - Servo parameters

2. **platformio.ini**
   - Build settings
   - Library versions
   - Upload configuration

## Development Setup

1. **Arduino IDE**
   - Install ESP32 board support
   - Configure serial port
   - Set upload speed

2. **PlatformIO**
   - Install required libraries
   - Configure build environment
   - Set up OTA updates

## First Time Setup

1. **Hardware**
   - Connect servo to GPIO13
   - Connect LED to GPIO2
   - Connect power supply

2. **Software**
   - Upload initial firmware
   - Configure WiFi
   - Test basic functions

## Maintenance

1. **Regular Checks**
   - Inspect connections
   - Test servo response
   - Monitor WiFi signal

2. **Updates**
   - Check for firmware updates
   - Update libraries
   - Backup configuration

## Future Improvements

1. **Hardware**
   - Add current monitoring
   - Implement failsafe
   - Add telemetry

2. **Software**
   - Enhance error handling
   - Add logging
   - Improve OTA process 