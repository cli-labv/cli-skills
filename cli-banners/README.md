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
- **Estilo Block**: Caracteres sólidos tipo FIGLET (6 líneas)
- **Estilo Slim**: Letras más delgadas (5 líneas)
- **Estilo Mini**: Compacto (3 líneas)
- **Estilo Simple**: ASCII puro sin unicode (5 líneas)
- **Estilo Minimal**: Caracteres de caja unicode (3 líneas)

### 🔤 Alfabeto Completo (alphabet.py)
- **A-Z completo** en todos los estilos
- **0-9 números** 
- **Símbolos**: ! ? . , : - _ / @ # + = * ( ) [ ] < > & % $ ' "
- Fácil de extender con nuevos caracteres

### 🖼️ Generación de Shapes
- **Formas geométricas**: Círculos, rectángulos, triángulos
- **Símbolos comunes**: Flechas, checkmarks, íconos
- **Figuras simples**: Estrellas, corazones, etc.

### 🎯 Estilos Configurables
- `block`: Bloques sólidos █ (6 líneas, el más legible)
- `slim`: Más delgado ▄▀ (5 líneas)
- `mini`: Compacto ▄█▀ (3 líneas, ideal para espacios reducidos)
- `simple`: ASCII puro /\-| (5 líneas, máxima compatibilidad)
- `minimal`: Box-drawing ┌┐└┘ (3 líneas)

### 🌈 Soporte de Colores
- Colores ANSI estándar
- Gradientes
- Resaltado de texto

## Uso Rápido

### Python - Básico

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

### Python - Modo Interactivo (NUEVO! ✨)

```python
from cli_banners import interactive_banner

# Solicita al usuario: estilo, color y animación
interactive_banner("WELCOME")
```

**Preguntas que hace:**
- 🎨 Seleccionar estilo: block, slim, mini, simple, minimal
- 🎨 Seleccionar color: red, green, cyan, yellow, magenta, white, etc.
- ✨ Seleccionar animación: none, typewriter, fade_in, bounce, spinner

### Python - Animaciones

```python
from cli_banners import (
    generate_text,
    animate_typewriter,
    animate_fade_in,
    animate_bounce,
    animate_spinner_loading
)

banner = generate_text("HELLO", style="block", color="cyan")

# Efecto typewriter (carácter por carácter)
animate_typewriter(banner, delay=0.05)

# Fade in (línea por línea)
animate_fade_in(banner, line_delay=0.1)

# Bounce (efecto rebote)
animate_bounce(banner, bounce_count=2, delay=0.15)

# Spinner (animación de carga)
animate_spinner_loading("Loading", duration=2.0, color="yellow")
```

### Python - Alfabeto Extendido

```python
# Usar el módulo de alfabeto completo
from alphabet import render_text, list_characters, STYLE_INFO

# Ver estilos disponibles
for name, info in STYLE_INFO.items():
    print(f"{name}: {info['description']}")

# Renderizar con diferentes estilos
print(render_text("HELLO", style="block", color="cyan"))
print(render_text("WORLD", style="slim", color="green"))
print(render_text("TEST", style="mini", color="yellow"))
print(render_text("ABC123", style="simple"))  # ASCII puro

# Ver caracteres disponibles
chars = list_characters('block')
print(f"Disponibles: {' '.join(chars)}")
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

### Animaciones (NUEVO! ✨)

#### `animate_typewriter(text, delay=0.05, color=None)`
Anima el banner con efecto máquina de escribir.

```python
banner = generate_text("HELLO", style="block")
animate_typewriter(banner, delay=0.02)
```

#### `animate_fade_in(text, line_delay=0.1, color=None)`
Anima el banner línea por línea.

```python
animate_fade_in(banner, line_delay=0.15)
```

#### `animate_bounce(text, bounce_count=2, delay=0.1, color=None)`
Anima el banner con efecto rebote.

```python
animate_bounce(banner, bounce_count=3, delay=0.2)
```

#### `animate_spinner_loading(text="Loading", frames=None, duration=2.0, color=None)`
Muestra un spinner animado.

```python
animate_spinner_loading("Processing", duration=2.0, color="cyan")
```

### Modo Interactivo (NUEVO! ✨)

#### `interactive_banner(text, use_questionary=True)`
Genera banner con selección interactiva de estilo, color y animación.

```python
# Pregunta al usuario qué opciones quiere
interactive_banner("WELCOME")
```

**Características:**
- 🎨 Selecciona estilo: block, slim, mini, simple
- 🎨 Selecciona color: red, green, cyan, yellow, magenta, etc.
- ✨ Selecciona animación: typewriter, fade_in, bounce, spinner, none

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

### Block Style (6 líneas - Recomendado)
```
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ██║   ██║██║     █████╔╝ 
██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
```

### Slim Style (5 líneas)
```
  ▄▄    █▀▀▄  ▄▄▄ 
 █▀▀█   █▀▀▄ █    
 █▄▄█   █▄▄▀ █    
 █  █   █     ▀▀▀ 
```

### Mini Style (3 líneas - Compacto)
```
▄█▄ ██▄ ▄█▀ 
█▀█ █▄█ █   
▀ ▀ ▀▀  ▀█▄ 
```

### Simple Style (ASCII puro)
```
  /\   |==\  ___ 
 /  \  |   )/    
/----\ |==< |    
|    | |   )\    
       |==/  --- 
```

### Minimal Style (3 líneas)
```
┌─┐┬  ┌─┐┌─┐┌┐┌
│  │  ├┤ ├─┤│││
└─┘┴─┘└─┘┴ ┴┘└┘
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
from cli_banners import generate_text, animate_fade_in

banner = generate_text("MYAPP", style="block", color="cyan")
animate_fade_in(banner, line_delay=0.1)
print("  Version 1.0.0 - Production Ready\n")
```

### 2. Mensajes de Estado
```python
from cli_banners import generate_shape, animate_typewriter

success = generate_shape("check", color="green")
error = generate_shape("cross", color="red")

print(f"{success} Deployment successful")
print(f"{error} Connection failed")

# Animado
animate_typewriter("✅ Processing completed!", delay=0.05, color="green")
```

### 3. Headers de Sección
```python
from cli_banners import generate_text, animate_bounce

title = generate_text("CONFIGURATION", style="minimal", color="blue")
animate_bounce(title, bounce_count=1)
print("─" * 50)
```

### 4. CLI Interactivos con Animaciones
```python
from cli_banners import interactive_banner

# El usuario selecciona estilo, color y animación
interactive_banner("MENU")
```

### 5. Carga con Spinner
```python
from cli_banners import animate_spinner_loading, generate_text

animate_spinner_loading("Initializing system", duration=2.0, color="cyan")

banner = generate_text("READY", style="block", color="green")
print(banner)
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
✅ **Animaciones**: Typewriter, fade-in, bounce, spinner  
✅ **Interactivo**: Selecciona estilo, color y animación (con questionary)  
✅ **Ligero**: ~1000 líneas de código puro  
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

### Versión 1.1 (NUEVA! ✨)
- [x] Animaciones de texto (typewriter, fade-in, bounce, spinner)
- [x] Modo interactivo con questionary
- [x] Selector de estilo y color
- [x] Selección de tipo de animación

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
