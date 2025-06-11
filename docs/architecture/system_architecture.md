# System Architecture

This document outlines the system architecture of the RC Vehicle Immersive project.

## System Components

### 1. Motor Control Unit (Arduino Nano ESP32)
- **Hardware**
  - Arduino Nano ESP32
  - Steering servo
  - Status LED
  - WiFi connectivity

- **Software**
  - Servo Controller
  - WiFi Manager
  - OTA Update Handler
  - Status Monitor

### 2. Control System (Laptop)
- **Hardware**
  - Computer with WiFi
  - Joystick controller
  - Display for video feed

- **Software**
  - Joystick Control Interface
  - Video Viewer
  - UDP Sender
  - Configuration Manager

### 3. Video System (Jetson)
- **Hardware**
  - NVIDIA Jetson
  - Camera
  - WiFi connectivity

- **Software**
  - Video Streamer
  - UDP Receiver
  - Camera Controller
  - Network Manager

## Communication Architecture

### 1. Control Channel
- Protocol: UDP
- Port: 8888
- Direction: Laptop → Arduino
- Data: Steering commands

### 2. Video Channel
- Protocol: UDP
- Port: 8889
- Direction: Jetson → Laptop
- Data: Video stream

### 3. OTA Updates
- Protocol: HTTP
- Port: 3232
- Direction: Laptop → Arduino
- Data: Firmware updates

## Data Formats

### 1. UART Commands
```
S<angle>  # Set steering angle (0-180)
C         # Center steering
T         # Run sweep test
```

### 2. UDP Control Packets
```json
{
  "command": "steer",
  "angle": 90,
  "timestamp": 1234567890
}
```

### 3. Video Stream
- Format: H.264
- Resolution: 720p
- Frame Rate: 30 FPS
- Bitrate: 2 Mbps

## Security Considerations

1. **Network Security**
   - WPA2 encryption
   - Secure OTA updates
   - Command validation

2. **Data Protection**
   - Encrypted communication
   - Secure credentials
   - Access control

3. **System Safety**
   - Failsafe mechanisms
   - Error handling
   - Watchdog timers

## Performance Considerations

1. **Latency**
   - Control: < 50ms
   - Video: < 100ms
   - OTA: < 5s

2. **Bandwidth**
   - Control: < 1 Kbps
   - Video: 2 Mbps
   - OTA: 1 Mbps

3. **Resource Usage**
   - CPU: < 50%
   - Memory: < 256MB
   - Storage: < 1GB

## Future Extensions

1. **VR Integration**
   - Head tracking
   - Immersive view
   - Haptic feedback

2. **Autonomous Features**
   - Path planning
   - Obstacle avoidance
   - Auto-return

3. **Telemetry**
   - Battery monitoring
   - Speed tracking
   - GPS integration

## Development Guidelines

1. **Code Organization**
   - Modular design
   - Clear interfaces
   - Version control

2. **Testing**
   - Unit tests
   - Integration tests
   - Performance tests

3. **Documentation**
   - Code comments
   - API documentation
   - User guides

## Deployment

1. **Hardware Setup**
   - Component assembly
   - Power management
   - Network configuration

2. **Software Deployment**
   - Firmware upload
   - Configuration
   - Testing

3. **Maintenance**
   - Regular updates
   - Performance monitoring
   - Backup procedures 