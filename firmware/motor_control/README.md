# Motor Control Firmware

Firmware para el control de dirección del vehículo RC usando Arduino Nano ESP32.

## Requisitos

### Hardware
- Arduino Nano ESP32
- Servo de dirección
- LED indicador (GPIO2)
- Fuente de alimentación 5V
- Cable USB-C para programación

### Software
- Arduino IDE 2.0+ o PlatformIO
- ESP32 Board Support Package
- Bibliotecas requeridas:
  - ESP32Servo (v0.13.0)
  - ArduinoOTA (v1.0.0)
  - ArduinoJson (v6.21.3)

## Configuración

### 1. Preparación del Entorno

#### Usando Arduino IDE
1. Instalar Arduino IDE 2.0 o superior
2. Agregar soporte para ESP32:
   - Abrir Preferencias
   - Agregar URL: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
   - Instalar "ESP32" desde el Gestor de Tarjetas
3. Instalar bibliotecas requeridas:
   - ESP32Servo
   - ArduinoOTA
   - ArduinoJson

#### Usando PlatformIO
1. Instalar PlatformIO IDE
2. Clonar este repositorio
3. Abrir la carpeta del proyecto
4. PlatformIO instalará automáticamente las dependencias

### 2. Configuración del Hardware

1. Conectar el servo al pin GPIO13
2. Conectar el LED al pin GPIO2
3. Conectar la alimentación 5V
4. Conectar el cable USB-C

### 3. Configuración del Software

1. Crear archivo `config.h` con las credenciales WiFi:
```cpp
#define WIFI_SSID "tu_ssid"
#define WIFI_PASSWORD "tu_password"
```

2. Ajustar parámetros del servo si es necesario:
```cpp
#define SERVO_MIN_PULSE 500
#define SERVO_MAX_PULSE 2400
#define SERVO_FREQ 50
```

## Uso

### Comandos Seriales
- `S<ángulo>`: Mover servo a ángulo específico (0-180)
- `C`: Centrar servo (90 grados)
- `TEST`: Ejecutar prueba de barrido completo

### Actualizaciones OTA
1. Asegurarse que el Arduino está conectado a WiFi
2. Usar Arduino IDE o PlatformIO para subir actualizaciones
3. Verificar el progreso en el monitor serial

## Solución de Problemas

### Servo no responde
1. Verificar conexiones de alimentación
2. Comprobar señal en el pin GPIO13
3. Verificar inicialización de la biblioteca ESP32Servo
4. Comprobar valores de pulso en config.h

### WiFi no conecta
1. Verificar credenciales en config.h
2. Comprobar señal WiFi
3. Verificar que el ESP32 está en modo estación
4. Revisar logs en monitor serial

### OTA no funciona
1. Verificar conexión WiFi
2. Comprobar que el Arduino es accesible en la red
3. Verificar que el puerto 3232 está abierto
4. Revisar logs de error en monitor serial

## Desarrollo

### Estructura del Código
- `motor_control.ino`: Código principal
- `config.h`: Configuración y credenciales
- `platformio.ini`: Configuración de PlatformIO

### Flujo de Control
1. Inicialización de hardware
2. Conexión WiFi
3. Configuración OTA
4. Bucle principal:
   - Manejo de comandos seriales
   - Control de servo
   - Actualizaciones OTA
   - Feedback LED

## Contribución
1. Fork el repositorio
2. Crear rama para feature
3. Commit cambios
4. Push a la rama
5. Crear Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](../LICENSE) para más detalles. 