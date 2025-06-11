# Guía de Inicio del Sistema RC Vehicle

Esta guía detalla el proceso paso a paso para iniciar y verificar el sistema RC Vehicle.

## Prerrequisitos

### Hardware
1. Arduino Nano ESP32 con firmware instalado
2. Joystick compatible con Windows
3. Cámara USB conectada al Jetson
4. Jetson Nano/Orin con sistema operativo instalado
5. Laptop con Windows 10/11
6. Red WiFi configurada

### Software
1. Python 3.8+ instalado en laptop y Jetson
2. Dependencias instaladas:
   - En laptop: `pip install -r laptop/requirements.txt`
   - En Jetson: `pip install -r jetson/requirements.txt`
3. Firmware Arduino actualizado
4. Conexión WiFi estable

## Secuencia de Inicio

### 1. Preparación del Arduino
1. Conectar el Arduino a la fuente de alimentación
2. Verificar que el LED de estado parpadee durante el inicio
3. Esperar a que el LED se mantenga encendido (indica conexión WiFi)
4. Anotar la dirección IP del Arduino (mostrada en el monitor serial)

### 2. Preparación del Jetson
1. Encender el Jetson
2. Conectar la cámara USB
3. Verificar que la cámara sea detectada:
   ```bash
   ls /dev/video*
   ```
4. Configurar la dirección IP del Jetson:
   - Editar `jetson/video_streaming/video_streamer.py`
   - Actualizar `UDP_IP` con la dirección IP de la laptop
   - Actualizar `UDP_PORT` si es necesario

### 3. Preparación de la Laptop
1. Configurar el control del joystick:
   - Editar `laptop/joystick_control/send_joystick.py`
   - Actualizar `UDP_IP` con la dirección IP del Jetson
   - Actualizar `UDP_PORT` si es necesario

2. Configurar el visor de video:
   - Editar `laptop/video_viewer/view_stream.py`
   - Verificar que `UDP_PORT` coincida con el del Jetson

## Verificación del Sistema

### 1. Iniciar el Video Stream
1. En el Jetson, ejecutar:
   ```bash
   cd jetson/video_streaming
   python video_streamer.py
   ```
2. Verificar que no haya errores de conexión
3. Confirmar que la cámara esté capturando video

### 2. Iniciar el Visor de Video
1. En la laptop, ejecutar:
   ```bash
   cd laptop/video_viewer
   python view_stream.py
   ```
2. Verificar que se muestre la ventana del video
3. Confirmar que el FPS sea estable

### 3. Iniciar el Control del Joystick
1. En la laptop, ejecutar:
   ```bash
   cd laptop/joystick_control
   python send_joystick.py
   ```
2. Verificar que el joystick sea detectado
3. Probar los controles:
   - Mover el joystick izquierdo para dirección
   - Presionar A para centrar
   - Presionar B para salir

## Solución de Problemas

### 1. Problemas de Video
- Verificar conexión de la cámara
- Comprobar permisos de acceso
- Revisar configuración de resolución
- Verificar ancho de banda de la red

### 2. Problemas de Control
- Verificar conexión del joystick
- Comprobar configuración de IP
- Revisar puertos UDP
- Verificar conexión WiFi

### 3. Problemas de Arduino
- Verificar alimentación
- Comprobar conexión WiFi
- Revisar monitor serial
- Verificar firmware

## Apagado Seguro

1. Detener el control del joystick (presionar B)
2. Cerrar el visor de video (presionar Q)
3. Detener el video stream (Ctrl+C)
4. Apagar el Arduino
5. Apagar el Jetson

## Notas Importantes

1. **Seguridad**
   - Mantener las credenciales WiFi seguras
   - No exponer el sistema a redes públicas
   - Mantener el firmware actualizado

2. **Rendimiento**
   - Monitorear el uso de CPU
   - Verificar la latencia de red
   - Ajustar calidad de video si es necesario

3. **Mantenimiento**
   - Limpiar la cámara regularmente
   - Verificar conexiones
   - Actualizar software
   - Hacer backup de configuraciones

## Tareas de Mantenimiento

### Diarias
- Verificar conexiones
- Limpiar lente de cámara
- Probar controles básicos

### Semanales
- Actualizar software
- Verificar logs
- Probar todas las funciones

### Mensuales
- Revisar hardware
- Actualizar firmware
- Hacer backup de datos 