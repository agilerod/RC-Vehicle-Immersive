# Guía de Inicio del Sistema RC Vehicle

Esta guía detalla el proceso paso a paso para iniciar y verificar el sistema RC Vehicle.

## Prerrequisitos

### Hardware
1. Arduino Nano ESP32 con firmware instalado
2. Joystick compatible con Windows
3. Raspberry Pi Camera v2 con interfaz CSI
4. Jetson Nano/Orin con sistema operativo instalado
5. Laptop con Windows 10/11
6. Cable CSI para la cámara
7. Cable USB-C para Arduino
8. Fuente de alimentación para Arduino
9. Red WiFi configurada

### Software
1. Python 3.8+ instalado en laptop y Jetson
2. Dependencias instaladas:
   - En laptop: `pip install -r laptop/requirements.txt`
   - En Jetson: `pip install -r jetson/requirements.txt`
3. Firmware Arduino actualizado
4. Conexión WiFi estable

### Network Configuration
- Jetson IP: 192.168.1.100 (static)
- Laptop IP: 192.168.1.101 (static)
- Arduino IP: 192.168.1.102 (static)
- Subnet: 255.255.255.0
- Gateway: 192.168.1.1

## Secuencia de Inicio

### 1. Preparación del Arduino
1. Conectar Arduino Nano ESP32 a laptop vía USB-C
2. Abrir Arduino IDE o PlatformIO
3. Cargar motor_control.ino
4. Verificar credenciales WiFi en config.h
5. Subir firmware
6. Verificar LED de estado:
   - Fijo: Listo
   - Parpadeo: Conectando WiFi
   - Parpadeo rápido: Error

### 2. Configuración del Jetson
1. Encender dispositivo Jetson
2. Conectar Raspberry Pi Camera v2 vía interfaz CSI
3. Verificar conexión de cámara:
   ```bash
   v4l2-ctl --list-devices
   ```
4. Iniciar streaming de video:
   ```bash
   python3 video_streamer.py
   ```
5. Verificar que el stream está activo:
   - Revisar salida de terminal por "Streaming started"
   - Verificar que puerto UDP 5000 está abierto

### 3. Configuración de Laptop
1. Abrir terminal en directorio laptop
2. Instalar requerimientos:
   ```bash
   pip install -r requirements.txt
   ```
3. Iniciar visor de video:
   ```bash
   python view_stream.py
   ```
4. Iniciar control de joystick:
   ```bash
   python send_joystick.py
   ```

### 4. Verificación del Sistema
1. Revisar stream de video:
   - Ventana debe mostrar feed en vivo
   - Sin retraso significativo
   - Calidad de imagen clara
2. Probar joystick:
   - Mover joystick
   - Verificar respuesta LED Arduino
   - Revisar movimiento del servo
3. Verificar Arduino:
   - LED de estado fijo
   - Servo responde a comandos
   - Sin mensajes de error en monitor serial

## Solución de Problemas

### Problemas de Video
1. Sin feed de video:
   - Revisar conexión CSI
   - Verificar que cámara está habilitada en Jetson
   - Revisar conectividad de red
   - Verificar puerto UDP 5000
2. Mala calidad de video:
   - Revisar cable CSI por daños
   - Verificar enfoque de cámara
   - Revisar ancho de banda de red
3. Alta latencia:
   - Reducir resolución de video
   - Revisar congestión de red
   - Verificar rendimiento Jetson

### Problemas de Control
1. Joystick no detectado:
   - Revisar conexión USB
   - Verificar que joystick es reconocido por OS
   - Revisar paquete Python inputs
2. Sin respuesta del vehículo:
   - Verificar conexión UDP
   - Revisar LED de estado Arduino
   - Verificar conexiones del servo
3. Movimiento errático:
   - Revisar calibración del joystick
   - Verificar límites del servo
   - Revisar por interferencia

### Problemas de Arduino
1. Fallo de conexión WiFi:
   - Revisar credenciales
   - Verificar disponibilidad de red
   - Revisar fuente de alimentación
2. Servo no responde:
   - Revisar fuente de alimentación
   - Verificar conexiones
   - Revisar límites del servo
3. Fallo de actualización OTA:
   - Revisar estabilidad de red
   - Verificar tamaño de firmware
   - Revisar memoria Arduino

## Apagado Seguro
1. Detener control de joystick (Ctrl+C)
2. Detener visor de video (Ctrl+C)
3. Detener streamer de video en Jetson (Ctrl+C)
4. Apagar Arduino
5. Apagar Jetson
6. Desconectar fuente de alimentación

## Notas Importantes

1. **Seguridad**
   - Cambiar credenciales WiFi por defecto
   - Usar direcciones IP estáticas
   - Mantener firmware actualizado
   - Monitorear tráfico de red
   - Asegurar actualizaciones OTA

2. **Rendimiento**
   - Mantener línea de vista
   - Monitorear niveles de batería
   - Revisar latencia de red
   - Monitorear recursos del sistema
   - Mantenimiento regular

3. **Mantenimiento**
   - Diario:
     - Revisar conexiones
     - Verificar enfoque de cámara
     - Probar controles
     - Revisar niveles de batería
   - Semanal:
     - Actualizar firmware
     - Limpiar lente de cámara
     - Revisar operación del servo
     - Verificar configuración de red
   - Mensual:
     - Prueba completa del sistema
     - Actualizar documentación
     - Respaldo de configuraciones
     - Revisar desgaste de hardware 