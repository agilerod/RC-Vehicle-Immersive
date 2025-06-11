# Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto RC Vehicle Immersive! Este documento proporciona las pautas y el proceso para contribuir.

## Código de Conducta

Este proyecto y todos los participantes se rigen por nuestro Código de Conducta. Al participar, se espera que respetes este código.

## Proceso de Contribución

### 1. Reportar un Bug

Si encuentras un bug, por favor:
1. Verifica que no haya sido reportado ya en los Issues
2. Usa el template de bug report
3. Incluye pasos para reproducir
4. Describe el comportamiento esperado vs actual
5. Incluye capturas de pantalla si es relevante

### 2. Sugerir una Mejora

Para sugerir una mejora:
1. Verifica que no haya sido sugerida ya
2. Usa el template de feature request
3. Describe el problema que resuelve
4. Incluye ejemplos de uso si es posible

### 3. Pull Request

Para enviar un PR:
1. Fork el repositorio
2. Crea una rama descriptiva (`feature/`, `fix/`, `docs/`)
3. Haz commits atómicos con mensajes claros
4. Asegúrate que los tests pasen
5. Actualiza la documentación si es necesario
6. Envía el PR con una descripción clara

## Estándares de Código

### Python
- PEP 8 para estilo
- Docstrings para funciones y clases
- Tests unitarios para nueva funcionalidad
- Type hints cuando sea posible

### Arduino
- Comentarios descriptivos
- Nombres de variables en inglés
- Documentación de pines y conexiones
- Manejo de errores robusto

### Documentación
- Markdown para archivos .md
- Incluir ejemplos de uso
- Mantener actualizada la guía de inicio
- Documentar cambios en el hardware

## Estructura del Proyecto

Mantén la estructura actual del proyecto:
```
RC-Vehicle-Immersive/
├── docs/                    # Documentación
├── firmware/               # Código Arduino
├── jetson/                 # Código Jetson
├── laptop/                 # Código Laptop
├── hardware/              # Esquemáticos
└── unity-vr-interface/    # Unity VR
```

## Licencia

Al contribuir, aceptas que tu contribución será licenciada bajo la Licencia MIT del proyecto. 