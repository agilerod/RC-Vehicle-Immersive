# Hardware Connections

This document details the hardware connections and pin configurations for the RC Vehicle Immersive project.

## Components

### Arduino Nano ESP32
- Microcontroller: ESP32-S3
- WiFi: 2.4GHz 802.11b/g/n
- USB: USB-C
- GPIO: 13 (Servo), 2 (Status LED)
- Power: 5V via USB or external supply
- Features:
  - WiFi connectivity
  - OTA updates
  - Servo control
  - Status LED

### Raspberry Pi Camera v2
- Interface: CSI
- Resolution: 1080p
- Frame Rate: 30fps
- Connection: CSI ribbon cable
- Power: 3.3V via CSI interface
- Features:
  - Auto-focus
  - H.264 encoding
  - Low latency

### Jetson Device
- Processor: NVIDIA Jetson
- Camera Interface: CSI
- Network: Ethernet/WiFi
- USB: Multiple ports
- Power: 12V DC
- Features:
  - Video processing
  - Network streaming
  - GPIO control

## Pin Connections

### Arduino Nano ESP32
| Component | GPIO Pin | Function |
|-----------|----------|----------|
| Servo | GPIO13 | PWM Control |
| Status LED | GPIO2 | System Status |
| USB | USB-C | Programming/Power |

### Raspberry Pi Camera v2
| Component | Connection | Function |
|-----------|------------|----------|
| CSI Interface | CSI Port | Video Data |
| Power | CSI Interface | 3.3V Power |
| I2C | CSI Interface | Camera Control |

### Jetson Device
| Component | Connection | Function |
|-----------|------------|----------|
| Camera | CSI Port | Video Input |
| Network | Ethernet/WiFi | Data Transfer |
| Power | DC Jack | 12V Power |

## Power Requirements

### Arduino Nano ESP32
- Operating Voltage: 5V
- Current Draw:
  - Base: 100mA
  - WiFi: 150mA
  - Servo: 500mA (peak)
- Total: 750mA (peak)

### Raspberry Pi Camera v2
- Operating Voltage: 3.3V
- Current Draw: 250mA
- Power Source: CSI Interface

### Jetson Device
- Operating Voltage: 12V
- Current Draw: 2A
- Power Source: DC Adapter

## Network Configuration

### Arduino Nano ESP32
- Protocol: WiFi
- Mode: Station
- Security: WPA2
- OTA: Enabled
- Static IP: 192.168.1.102

### Jetson Device
- Protocol: Ethernet/WiFi
- Mode: Access Point
- Security: WPA2
- Static IP: 192.168.1.100
- Ports:
  - 5000: Video Stream
  - 5001: Control Data

## Safety Considerations

### Electrical Safety
1. Power Supply
   - Use regulated power supplies
   - Check voltage ratings
   - Verify current capacity
   - Use proper connectors

2. Wiring
   - Secure all connections
   - Check for shorts
   - Use appropriate gauge
   - Label all wires

3. Camera
   - Handle CSI cable carefully
   - Avoid bending ribbon cable
   - Check camera orientation
   - Verify power supply

### Mechanical Safety
1. Servo Mounting
   - Secure mounting
   - Check range of motion
   - Verify connections
   - Test limits

2. Camera Mounting
   - Secure mounting
   - Check field of view
   - Protect from vibration
   - Verify focus

3. General
   - Check all fasteners
   - Verify stability
   - Test movement
   - Inspect regularly

## Troubleshooting

### Camera Issues
1. No Video
   - Check CSI connection
   - Verify camera power
   - Check Jetson settings
   - Test with v4l2-ctl

2. Poor Quality
   - Check focus
   - Verify resolution
   - Check lighting
   - Inspect CSI cable

3. Connection Issues
   - Check CSI port
   - Verify cable integrity
   - Check camera orientation
   - Test with known good camera

### Arduino Issues
1. Power Problems
   - Check voltage
   - Verify current
   - Check connections
   - Test power supply

2. WiFi Issues
   - Check credentials
   - Verify signal
   - Check IP address
   - Test connection

3. Servo Issues
   - Check power
   - Verify connections
   - Test PWM signal
   - Check limits

### Jetson Issues
1. Camera Detection
   - Check CSI port
   - Verify camera power
   - Check system logs
   - Test with v4l2-ctl

2. Network Issues
   - Check IP settings
   - Verify firewall
   - Test connectivity
   - Check ports

3. Performance
   - Monitor CPU usage
   - Check memory
   - Verify cooling
   - Test video pipeline

## Configuration Files

### Arduino
- config.h: WiFi settings
- motor_control.ino: Main firmware
- platformio.ini: Build settings

### Jetson
- video_streamer.py: Camera settings
- udp_receiver.py: Network settings
- requirements.txt: Dependencies

### Laptop
- view_stream.py: Display settings
- send_joystick.py: Control settings
- requirements.txt: Dependencies

## Development Setup

### Arduino IDE
1. Install Arduino IDE 2.0+
2. Add ESP32 board support
3. Install required libraries
4. Configure build settings

### PlatformIO
1. Install PlatformIO
2. Configure platformio.ini
3. Install dependencies
4. Set up build environment

### First Time Setup
1. Connect hardware
2. Verify connections
3. Upload firmware
4. Test functionality
5. Configure network
6. Verify operation

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