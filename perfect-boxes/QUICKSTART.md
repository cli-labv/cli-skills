# ⚡ Quick Start Guide - Perfect Boxes Skill

¿Quieres usar la skill inmediatamente? Esta guía de 5 minutos te tiene cubierto.

---

## 🚀 Inicio en 30 Segundos

### Python

```python
# 1. Agregar al path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "skills/perfect-boxes/python"))

# 2. Importar
from perfect_box import print_perfect_box

# 3. ¡Usar!
print_perfect_box("📸 MI APP", "¡Funciona!", width=50)
```

### Bash

```bash
# 1. Cargar
source skills/perfect-boxes/bash/perfect_banner.sh

# 2. ¡Usar!
print_perfect_box "📸 MI APP" "¡Funciona!"
```

---

## 📝 Tres Funciones Esenciales

### 1️⃣ `print_perfect_box()` - Cuadro Completo

```python
print_perfect_box(
    title="📸 TÍTULO",
    subtitle="Subtítulo opcional",
    description="Descripción opcional",
    width=60,
    color="cyan"
)
```

**Resultado:**
```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                      📸 TÍTULO                           ║
║                                                          ║
║                  Subtítulo opcional                      ║
║                                                          ║
║                 Descripción opcional                     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

### 2️⃣ `print_fancy_banner()` - Banner Simple

```python
print_fancy_banner("🚀 MI PROYECTO", "Versión 1.0", width=60)
```

**Resultado:**
```
════════════════════════════════════════════════════════════
                      🚀 MI PROYECTO
                        Versión 1.0
════════════════════════════════════════════════════════════
```

### 3️⃣ `print_header()` - Encabezado de Sección

```python
print_header("📋 Paso 1: Configuración", icon="⚙️", color="yellow")
```

**Resultado:**
```
⚙️  📋 Paso 1: Configuración
──────────────────────────────────────────────────
```

---

## 🎨 Colores Disponibles

```python
# Opciones: "cyan", "green", "yellow", "red", "blue", "magenta"

print_perfect_box("Info", color="cyan")     # Azul claro
print_perfect_box("Éxito", color="green")   # Verde
print_perfect_box("Aviso", color="yellow")  # Amarillo
print_perfect_box("Error", color="red")     # Rojo
print_perfect_box("Nota", color="blue")     # Azul
print_perfect_box("Especial", color="magenta")  # Magenta
```

---

## 💡 Ejemplos Comunes

### Script de Bienvenida

```python
from perfect_box import print_fancy_banner, print_header

print_fancy_banner("🚀 MI APP CLI", "Versión 2.0.0", width=70)
print()
print_header("📋 Menú Principal", color="cyan")
print("  1. Opción A")
print("  2. Opción B")
print("  3. Salir")
```

### Mensaje de Éxito

```python
from perfect_box import print_perfect_box

print_perfect_box(
    title="✅ PROCESO COMPLETADO",
    subtitle="Todos los archivos fueron procesados",
    description="Tiempo: 2.5 segundos",
    width=65,
    color="green"
)
```

### Mensaje de Error

```python
print_perfect_box(
    title="❌ ERROR",
    subtitle="No se pudo conectar al servidor",
    description="Código: 503 - Reintentar en 30 segundos",
    width=65,
    color="red"
)
```

### Progreso de Tareas

```python
print_header("🔄 Ejecutando tareas", color="cyan")
print("  ✅ Tarea 1: Completada")
print("  ✅ Tarea 2: Completada")
print("  ⏳ Tarea 3: En progreso...")
```

---

## 🐚 Bash: Ejemplo Completo

```bash
#!/usr/bin/env bash

# Cargar la skill
source "$(dirname "$0")/skills/perfect-boxes/bash/perfect_banner.sh"

# Banner de inicio
print_fancy_banner "🚀 SCRIPT DE DEPLOY" "Producción v1.0" 70

echo ""

# Header de sección
print_header "📦 Construyendo proyecto" "🔨"
npm run build
echo ""

# Verificar resultado
if [ $? -eq 0 ]; then
    print_perfect_box "✅ BUILD EXITOSO" "Proyecto construido correctamente" "" 60 "$COLOR_GREEN"
else
    print_perfect_box "❌ BUILD FALLIDO" "Revisa los logs para más detalles" "" 60 "$COLOR_RED"
    exit 1
fi

echo ""
print_header "🚀 Desplegando a servidor" "🌐"
# Comando de deploy...

echo ""
print_perfect_box "🎉 DEPLOY COMPLETADO" "La aplicación está en línea" "URL: https://miapp.com" 70 "$COLOR_GREEN"
```

---

## 🔍 Ver la Demo

Para ver todos los ejemplos visuales:

```bash
# Demo completa (recomendado)
python3 skills/perfect-boxes/showcase.py

# Demo de aplicación real
python3 skills/perfect-boxes/demo_app.py

# Ejecutar tests
python3 skills/perfect-boxes/python/test_perfect_box.py
```

---

## 📚 Más Información

- **Documentación completa:** `README.md`
- **Guía de integración:** `INTEGRATION.md`
- **Resumen del proyecto:** `PROJECT_SUMMARY.md`
- **Ejemplos:** `examples/`

---

## ❓ Preguntas Frecuentes

### ¿Por qué necesito esta skill?

Si usas emojis en tus cuadros Unicode, **necesitas** esta skill. Los emojis ocupan 2 celdas en terminal, pero Python/Bash los cuentan como 1 carácter, causando desalineación.

### ¿Tiene dependencias?

**No.** Solo usa la librería estándar de Python y Bash puro.

### ¿Funciona en Windows?

**Sí**, pero necesitas un terminal con soporte UTF-8 (Windows Terminal recomendado).

### ¿Puedo cambiar los caracteres del cuadro?

La skill usa caracteres Unicode estándar (╔ ═ ╗ ║ ╚ ╝). Para personalizarlos, modifica las constantes en el código fuente.

### ¿Qué versiones de Python soporta?

Python 3.7+ (no usa f-strings para máxima compatibilidad).

---

## 🎯 Resumen Ultra-Rápido

1. **Cargar:** `source skills/perfect-boxes/bash/perfect_banner.sh` (Bash) o importar (Python)
2. **Usar:** `print_perfect_box "Título" "Subtítulo"`
3. **Personalizar:** Ajustar `width`, `color`, agregar `icon`
4. **¡Listo!** Cuadros perfectos con emojis ✅

---

**¿Dudas?** Lee el `README.md` completo para detalles técnicos.

**¡Disfruta de tus cuadros perfectos!** 📦✨
