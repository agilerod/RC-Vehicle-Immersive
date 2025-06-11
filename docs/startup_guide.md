# Guía de Inicio del Sistema RC Vehicle Immersive

Esta guía describe el proceso paso a paso para poner en funcionamiento el sistema completo.

## Prerequisitos

### Hardware
1. Verificar que todos los componentes estén correctamente conectados:
   - Jetson Nano con cámara CSI
   - Arduino Nano ESP32 con servo
   - Laptop con joystick G29
   - Red WiFi funcionando

### Software
1. En la Laptop:
   - Python 3.8+ instalado
   - Dependencias instaladas: `pip install -r laptop/requirements.txt`
   - VLC instalado (para visualización alternativa)

2. En la Jetson:
   - JetPack 4.6+ instalado
   - GStreamer instalado: `sudo apt-get install gstreamer1.0-tools`
   - Python 3.8+ instalado

3. En el Arduino:
   - Firmware actualizado
   - Credenciales WiFi configuradas en `config.h`

## Secuencia de Inicio

### 1. Preparación del Arduino
1. Conectar Arduino Nano ESP32 a la alimentación
2. Verificar que el LED de estado parpadea (indica inicio)
3. Esperar conexión WiFi (LED se estabiliza)
4. Verificar en monitor serial (115200 baud):
   ```
   Iniciando prueba de servo y OTA...
   Servo inicializado correctamente
   Conectado a WiFi!
   IP: 192.168.68.xxx
   OTA listo
   ```

### 2. Inicio de la Jetson Nano
1. Encender la Jetson Nano
2. Esperar a que el sistema operativo inicie
3. Abrir una terminal y verificar la cámara:
   ```bash
   ls /dev/video*
   # Debería mostrar /dev/video0
   ```

4. Iniciar el stream de video:
   ```bash
   cd jetson/video_streaming
   ./stream_camera.sh
   ```
   - Verificar que no hay errores
   - El script debería mostrar información de streaming

5. En otra terminal, iniciar el receptor UDP:
   ```bash
   cd jetson/udp_receiver
   python udp_receiver.py
   ```
   - Debería mostrar "Esperando datos de joystick..."

### 3. Configuración de la Laptop
1. Abrir una terminal para el visor de video:
   ```bash
   cd laptop/video_viewer
   python view_stream.py
   ```
   - Verificar que se abre la ventana de video
   - Confirmar que hay señal de la cámara

2. En otra terminal, iniciar el control de joystick:
   ```bash
   cd laptop/joystick_control
   python send_joystick.py
   ```
   - Verificar que detecta el joystick G29
   - Debería mostrar "Joystick inicializado: Logitech G29"

### 4. Verificación del Sistema
1. Verificar conexión de video:
   - La ventana de video en la laptop debe mostrar la transmisión
   - Verificar que la latencia es aceptable (<200ms)

2. Verificar control de joystick:
   - Mover el volante del G29
   - Verificar que el receptor UDP en la Jetson muestra los valores
   - Verificar que el servo responde a los comandos

3. Verificar servo:
   - El servo debería moverse suavemente
   - El LED en el Arduino debería parpadear con cada comando

## Solución de Problemas

### Si el video no aparece:
1. Verificar que el script de streaming está corriendo
2. Comprobar la IP de la Jetson en la configuración
3. Verificar que el puerto 5000 está abierto
4. Probar con VLC como alternativa:
   ```bash
   vlc rtsp://192.168.68.101:5000
   ```

### Si el joystick no responde:
1. Verificar que el G29 está conectado
2. Comprobar que el script de joystick está corriendo
3. Verificar la IP de la Jetson en la configuración
4. Comprobar que el puerto 5005 está abierto

### Si el servo no se mueve:
1. Verificar que el Arduino está conectado a WiFi
2. Comprobar que el receptor UDP muestra los comandos
3. Verificar las conexiones del servo
4. Probar el comando de prueba en el Arduino:
   ```
   TEST
   ```

## Apagado Seguro

1. Detener el control de joystick (Ctrl+C)
2. Detener el visor de video (Ctrl+C)
3. Detener el stream de video en la Jetson (Ctrl+C)
4. Detener el receptor UDP (Ctrl+C)
5. Desconectar la alimentación del Arduino
6. Apagar la Jetson Nano

## Notas Importantes

1. **Orden de Inicio**:
   - Siempre iniciar primero el Arduino
   - Luego la Jetson
   - Finalmente la laptop

2. **Verificación de IPs**:
   - Jetson: 192.168.68.101
   - Laptop: 192.168.68.100
   - Arduino: IP dinámica (verificar en monitor serial)

3. **Puertos Utilizados**:
   - Video: 5000 (RTSP)
   - Control: 5005 (UDP)
   - OTA: 3232

4. **Seguridad**:
   - Usar red WiFi privada
   - Cambiar credenciales por defecto
   - Mantener firmware actualizado

## Mantenimiento

1. **Diario**:
   - Verificar conexiones
   - Limpiar lente de la cámara
   - Comprobar batería

2. **Semanal**:
   - Actualizar firmware si hay nuevas versiones
   - Verificar logs de error
   - Calibrar servo si es necesario

3. **Mensual**:
   - Revisar todas las conexiones
   - Actualizar sistema operativo
   - Hacer backup de configuración 