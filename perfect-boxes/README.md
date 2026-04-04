# Perfect Boxes Skill 📦

## El Problema

Cuando dibujas cuadros en terminal usando caracteres Unicode (╔ ═ ╗ ║ ╚ ╝) y incluyes **emojis** o caracteres de ancho doble, los cuadros quedan desalineados:

### ❌ Incorrecto (Cuadro roto):
```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║ 📸 DIRTOPDF CLI 📄                                         ║  ← ¡Línea desalineada!
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### ✅ Correcto (Cuadro perfecto):
```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  📸 DIRTOPDF CLI 📄                                        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

## ¿Por qué ocurre?

Los emojis modernos (📸, 📄, 🚀, ✅, etc.) ocupan **2 celdas de ancho** en los terminales, pero:
- `len("📸")` retorna **1** (es 1 carácter Unicode)
- El terminal renderiza **2 celdas** de ancho

Entonces si calculas padding con:
```python
padding = total_width - len(text)  # ❌ Asume que emoji = 1 celda
```

El cuadro queda desalineado porque el emoji realmente ocupa 2 celdas.

## La Solución

Esta skill calcula el **ancho visual real** de cada carácter:
- ASCII/Letras normales = 1 celda
- Emojis/Caracteres anchos = 2 celdas
- Caracteres de control = 0 celdas

Luego ajusta el padding para que el cuadro cierre perfectamente.

## Uso

### Bash (Para scripts shell)

```bash
source skills/perfect-boxes/bash/perfect_banner.sh

# Cuadro simple
print_perfect_box "Mi Título" "Subtítulo opcional"

# Banner con emoji
print_fancy_banner "🚀 MI APP" "Versión 1.0"

# Header simple
print_header "📋 Paso 1: Configuración"
```

### Python (Recomendado para apps)

```python
from skills.perfect_boxes.python.perfect_box import (
    print_perfect_box,
    print_fancy_banner,
    print_header
)

# Cuadro completo con todos los parámetros
print_perfect_box(
    title="📸 DIRTOPDF CLI 📄",
    subtitle="Convierte Carpetas de Imágenes en PDFs",
    description="Versión 1.0.0",
    icon="🚀",
    width=60,
    color="cyan"
)

# Banner simple
print_fancy_banner("✅ Proceso completado", "Todos los archivos generados")

# Header de sección
print_header("📁 Preparando archivos...", icon="⚙️")
```

## Funciones Disponibles

### `print_perfect_box()`
Cuadro completo con título, subtítulo y descripción.

**Parámetros:**
- `title` (str): Título principal
- `subtitle` (str, opcional): Subtítulo
- `description` (str, opcional): Descripción adicional
- `icon` (str, opcional): Emoji para decorar
- `width` (int, opcional): Ancho del cuadro (default: 60)
- `color` (str, opcional): Color del texto (cyan, green, yellow, red)

### `print_fancy_banner()`
Banner decorativo con bordes superior e inferior.

**Parámetros:**
- `title` (str): Título principal
- `subtitle` (str, opcional): Subtítulo

### `print_header()`
Línea de encabezado simple para secciones.

**Parámetros:**
- `text` (str): Texto del header
- `icon` (str, opcional): Emoji decorativo

## Casos de Uso Soportados

✅ Solo texto ASCII  
✅ Texto con 1 emoji  
✅ Texto con múltiples emojis  
✅ Texto largo (múltiples líneas)  
✅ Caracteres Unicode especiales  
✅ Cuadros de diferente ancho  
✅ Banners abiertos (solo top/bottom)  

## Ejemplos Visuales

Ver la carpeta `examples/` para casos de uso completos con salida esperada.

## Implementación Técnica

### Bash
Usa una aproximación basada en regex para detectar emojis comunes y caracteres de ancho doble.

### Python
Implementa el algoritmo `wcwidth` estándar (UAX #11) para calcular el ancho visual exacto de cada carácter Unicode.

## Integración en Proyectos

### start.sh
```bash
#!/usr/bin/env bash

# Importar la skill
source skills/perfect-boxes/bash/perfect_banner.sh

# Usar en tu script
print_fancy_banner "🚀 MI PROYECTO" "Iniciando..."
```

### main.py
```python
from skills.perfect_boxes.python.perfect_box import print_perfect_box

def main():
    print_perfect_box(
        title="📸 Mi App CLI",
        subtitle="Bienvenido",
        width=70
    )
```

## Licencia

MIT - Reutilizable en cualquier proyecto.

## Autor

Creado como una skill reutilizable para resolver el problema común de desalineación de cuadros Unicode con emojis.
