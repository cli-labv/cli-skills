# CLI Banners - ASCII Art Generator Skill 🎨

## El Problema

Cuando necesitas crear banners y arte ASCII para CLIs profesionales, las opciones son limitadas:
- **Herramientas externas** como `figlet` requieren instalación
- **ASCII art manual** es tedioso y propenso a errores
- **Generadores online** no son reproducibles en scripts
- **Falta de consistencia** en estilos y calidad

## La Solución

Esta skill proporciona un **generador de ASCII art profesional** completamente integrado, sin dependencias externas.

### ✅ Correcto (con esta skill):
```
████████╗███████╗███████╗████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
   ██║   █████╗  ███████╗   ██║   
   ██║   ██╔══╝  ╚════██║   ██║   
   ██║   ███████╗███████║   ██║   
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
```

### ❌ Sin la skill:
```
TTTTT EEEEE SSSSS TTTTT
  T   E     S       T
  T   EEE   SSS     T
  T   E       S     T
  T   EEEEE SSSSS   T
```

## Características

### 🎨 Generación de Texto
- **Estilo Block**: Caracteres sólidos tipo FIGLET
- **Estilo Box**: Caracteres con bordes Unicode
- **Estilo Slant**: Texto inclinado elegante
- **Estilo Shadow**: Con efecto de sombra

### 🖼️ Generación de Shapes
- **Formas geométricas**: Círculos, rectángulos, triángulos
- **Símbolos comunes**: Flechas, checkmarks, íconos
- **Figuras simples**: Estrellas, corazones, etc.

### 🎯 Estilos Configurables
- `block`: Bloques sólidos █
- `shaded`: Con sombreado ░▒▓█
- `minimal`: Limpio y espaciado
- `detailed`: Refinado con detalles

### 🌈 Soporte de Colores
- Colores ANSI estándar
- Gradientes
- Resaltado de texto

## Uso Rápido

### Python

```python
from cli_banners import generate_text, generate_shape

# Generar texto
banner = generate_text("HELLO", style="block")
print(banner)

# Generar shape
arrow = generate_shape("arrow_right", style="block", size="medium")
print(arrow)

# Con color
banner_colored = generate_text("SUCCESS", style="block", color="green")
print(banner_colored)
```

### Bash

```bash
source skills/cli-banners/bash/banner_generator.sh

# Generar texto
generate_banner "HELLO" "block"

# Generar shape
generate_arrow "right" "block"

# Con color
generate_colored_banner "SUCCESS" "green"
```

## Funciones Disponibles

### Generación de Texto

#### `generate_text(text, style='block', color=None, width=None)`
Genera texto en ASCII art con el estilo especificado.

**Parámetros:**
- `text` (str): Texto a convertir
- `style` (str): "block", "box", "slant", "shadow", "minimal"
- `color` (str): Color ANSI opcional
- `width` (int): Ancho máximo (auto-ajusta)

**Ejemplo:**
```python
generate_text("CLI", style="block", color="cyan")
```

### Generación de Shapes

#### `generate_shape(shape_type, style='block', size='medium', color=None)`
Genera formas y símbolos en ASCII.

**Shapes disponibles:**
- `arrow_right`, `arrow_left`, `arrow_up`, `arrow_down`
- `check`, `cross`, `star`, `heart`
- `circle`, `square`, `triangle`
- `loading`, `spinner`

**Ejemplo:**
```python
generate_shape("arrow_right", style="shaded", size="large")
```

### Utilidades

#### `get_available_styles()`
Lista todos los estilos disponibles.

#### `get_available_shapes()`
Lista todas las formas disponibles.

#### `colorize(text, color)`
Aplica color ANSI a texto.

## Estilos de Texto

### Block Style
```
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ██║   ██║██║     █████╔╝ 
██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
```

### Box Style
```
╔═╗╦  ╔═╗╔═╗╔╗╔╔╦╗
║╣ ║  ║╣ ║ ╦╠╩╗║║║
╚═╝╩═╝╚═╝╚═╝╚═╝╝╚╝
```

### Minimal Style
```
┌─┐┬  ┌─┐┌─┐┌┐┌
│  │  ├┤ ├─┤│││
└─┘┴─┘└─┘┴ ┴┘└┘
```

### Shadow Style
```
░█▀▀░█░░░█▀▀░█▀▀░█▀█░▀█▀
░█░░░█░░░█▀▀░█▀█░█░█░░█░
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░▀░
```

## Shapes Disponibles

### Arrows
```
→ Arrow Right (minimal)
⇒ Arrow Right (block)
⟹ Arrow Right (detailed)

← ↑ ↓ (todas direcciones)
```

### Checkmarks
```
✓ Check (minimal)
✅ Check (block)
☑ Check (box)
```

### Loading/Spinners
```
⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏ (spinner frames)
▁▂▃▄▅▆▇█ (progress bar)
```

## Colores Soportados

- `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
- `bright_red`, `bright_green`, etc.
- Gradientes automáticos

## Casos de Uso

### 1. Banner de Bienvenida
```python
from cli_banners import generate_text

banner = generate_text("MYAPP", style="block", color="cyan")
print(banner)
print("  Version 1.0.0 - Production Ready\n")
```

### 2. Mensajes de Estado
```python
from cli_banners import generate_shape

success = generate_shape("check", color="green")
error = generate_shape("cross", color="red")
loading = generate_shape("spinner", style="animated")

print(f"{success} Deployment successful")
print(f"{error} Connection failed")
print(f"{loading} Processing...")
```

### 3. Headers de Sección
```python
title = generate_text("CONFIGURATION", style="minimal")
print(title)
print("─" * 50)
```

### 4. CLI Interactivos
```python
from cli_banners import generate_shape, generate_text

menu_title = generate_text("MENU", style="box")
arrow = generate_shape("arrow_right", size="small")

print(menu_title)
print(f"{arrow} Option 1")
print(f"{arrow} Option 2")
print(f"{arrow} Option 3")
```

## Integración con Otros Proyectos

### Con Perfect-Boxes
```python
from skills.perfect_boxes.python.perfect_box import print_perfect_box
from skills.cli_banners.python.cli_banners import generate_text

title = generate_text("MYAPP", style="minimal")
print_perfect_box(title, "Welcome Screen", width=70)
```

### En Scripts de Deployment
```bash
source skills/cli-banners/bash/banner_generator.sh

generate_colored_banner "DEPLOY" "cyan"
echo ""
echo "Starting deployment process..."
```

## Ventajas

✅ **Sin dependencias**: No requiere figlet, toilet, ni otros paquetes  
✅ **Reproducible**: Mismo resultado en cualquier entorno  
✅ **Personalizable**: Estilos y colores configurables  
✅ **Ligero**: ~500 líneas de código puro  
✅ **Profesional**: Calidad de herramientas comerciales  
✅ **Integrable**: Funciona con otras skills  

## Ejemplos Visuales

Ver la carpeta `examples/` para casos de uso completos.

## Implementación Técnica

### Python
- Algoritmos de renderizado de fuentes basados en matrices
- Sistema de estilos modular
- Soporte de colores ANSI completo

### Bash
- Funciones predefinidas para casos comunes
- Wrappers simples para uso rápido

## Limitaciones Conocidas

- Fuentes limitadas a las incluidas (block, box, minimal, shadow)
- No soporta fuentes TTF externas
- Shapes complejos requieren definición manual

## Roadmap

### Versión 1.1
- [ ] Más estilos de fuentes (3D, bubble, etc.)
- [ ] Generador de logos simples
- [ ] Animaciones de texto

### Versión 2.0
- [ ] Soporte de gradientes RGB
- [ ] Generación de QR codes en ASCII
- [ ] Editor interactivo

## Licencia

MIT - Reutilizable en cualquier proyecto.

## Ver También

- **perfect-boxes**: Para cuadros con emojis perfectos
- **figlet**: Herramienta externa alternativa (requiere instalación)
- **lolcat**: Para colores rainbow (requiere instalación)

---

**Creado como skill reutilizable para proyectos CLI profesionales.**
