# Guía de Integración: Perfect Boxes Skill

Esta guía muestra cómo integrar la skill `perfect-boxes` en diferentes tipos de proyectos.

## Tabla de Contenidos

1. [Integración en Bash Scripts](#bash-scripts)
2. [Integración en Python CLI](#python-cli)
3. [Integración en proyectos existentes](#proyectos-existentes)
4. [Resolución de problemas](#troubleshooting)

---

## 1. Integración en Bash Scripts

### Opción A: Source directo (recomendado para scripts pequeños)

```bash
#!/usr/bin/env bash

# Cargar la skill
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/skills/perfect-boxes/bash/perfect_banner.sh"

# Usar las funciones
print_fancy_banner "🚀 MI SCRIPT" "Iniciando proceso..."

echo ""
print_header "📋 Paso 1: Configuración" "⚙️"
echo "  Configurando variables..."

echo ""
print_perfect_box "✅ COMPLETADO" "Script ejecutado exitosamente" "" 60 "$COLOR_GREEN"
```

### Opción B: Instalación global (para uso en múltiples scripts)

1. Copiar las funciones a tu directorio de utilidades:
```bash
mkdir -p ~/.local/lib/bash
cp skills/perfect-boxes/bash/perfect_banner.sh ~/.local/lib/bash/
```

2. Crear un alias en tu `~/.bashrc`:
```bash
# En ~/.bashrc
alias load-boxes='source ~/.local/lib/bash/perfect_banner.sh'
```

3. Usar en cualquier script:
```bash
#!/usr/bin/env bash
source ~/.local/lib/bash/perfect_banner.sh

print_fancy_banner "🎯 MI PROYECTO"
```

---

## 2. Integración en Python CLI

### Opción A: Importación directa (estructura de proyecto)

```
mi-proyecto/
├── main.py
├── skills/
│   └── perfect-boxes/
│       └── python/
│           └── perfect_box.py
└── src/
    └── app.py
```

En tu `main.py`:
```python
import sys
from pathlib import Path

# Agregar skills al path
skills_path = Path(__file__).parent / "skills" / "perfect-boxes" / "python"
sys.path.insert(0, str(skills_path))

from perfect_box import print_perfect_box, print_header

def main():
    print_perfect_box(
        title="📸 MI APP CLI",
        subtitle="Bienvenido al sistema",
        width=70,
        color="cyan"
    )
    
    print_header("🚀 Iniciando proceso", color="green")
    # Tu código aquí...

if __name__ == "__main__":
    main()
```

### Opción B: Como módulo local

Crear un módulo de utilidades:

```python
# src/utils/ui.py
import sys
from pathlib import Path

# Cargar la skill
_skills_path = Path(__file__).parent.parent.parent / "skills" / "perfect-boxes" / "python"
sys.path.insert(0, str(_skills_path))

from perfect_box import (
    print_perfect_box as box,
    print_fancy_banner as banner,
    print_header as header
)

# Re-exportar con nombres más cortos
__all__ = ['box', 'banner', 'header']
```

Usar en tu app:
```python
# main.py
from src.utils.ui import box, banner, header

banner("🚀 MI APP", "Versión 1.0")
header("📋 Cargando configuración")
box("✅ Listo", "Configuración cargada", width=60)
```

### Opción C: Como paquete instalable

Si quieres distribuir la skill como paquete:

1. Crear `setup.py`:
```python
from setuptools import setup, find_packages

setup(
    name="perfect-boxes",
    version="1.0.0",
    packages=find_packages(),
    description="Draw perfect Unicode boxes with emoji support",
    author="Tu Nombre",
    python_requires=">=3.7",
)
```

2. Instalar en modo desarrollo:
```bash
cd skills/perfect-boxes
pip install -e .
```

3. Usar en cualquier proyecto:
```python
from perfect_box import print_perfect_box

print_perfect_box("📸 Test", width=60)
```

---

## 3. Integración en Proyectos Existentes

### Migración de cuadros existentes

Si ya tienes funciones de cuadros, así es como migrar:

**Antes:**
```python
def print_title(text):
    print("=" * 60)
    print(text.center(60))
    print("=" * 60)

print_title("📸 MI APP")  # ❌ Desalineado con emojis
```

**Después:**
```python
from perfect_box import print_fancy_banner

print_fancy_banner("📸 MI APP", width=60)  # ✅ Perfecto
```

### Refactorización paso a paso

1. **Identificar funciones de UI existentes:**
```bash
grep -r "print.*═\|print.*╔" src/
```

2. **Reemplazar con la skill:**
```python
# Antes
def show_welcome():
    print("╔════════╗")
    print("║ Welcome║")
    print("╚════════╝")

# Después
from perfect_box import print_perfect_box

def show_welcome():
    print_perfect_box("Welcome", width=40)
```

3. **Actualizar tests:**
```python
# test_ui.py
def test_welcome_message(capsys):
    show_welcome()
    captured = capsys.readouterr()
    assert "╔" in captured.out
    assert "Welcome" in captured.out
    assert "╚" in captured.out
```

---

## 4. Resolución de Problemas

### Problema: Cuadros desalineados en Windows

**Solución:** Usar `chcp 65001` para UTF-8:
```bash
@echo off
chcp 65001 > nul
python main.py
```

### Problema: Emojis no se ven correctamente

**Causa:** Terminal sin soporte Unicode  
**Solución:** Usar terminal moderno (Windows Terminal, iTerm2, Alacritty)

### Problema: ImportError al importar perfect_box

**Solución:** Verificar el path:
```python
import sys
from pathlib import Path

# Debug
print("Python path:", sys.path)

# Agregar el path correcto
skills_path = Path(__file__).parent / "skills" / "perfect-boxes" / "python"
print("Skills path:", skills_path, "Exists:", skills_path.exists())
sys.path.insert(0, str(skills_path))
```

### Problema: Los tests fallan con "ancho incorrecto"

**Causa:** Algunos emojis tienen variantes de ancho  
**Solución:** Actualizar la función `get_char_width()` para tu terminal específico.

---

## Ejemplos de Uso Real

### CLI de Backup

```python
from perfect_box import print_header, print_perfect_box

def run_backup():
    print_header("💾 Iniciando backup", icon="🔄")
    
    # Proceso de backup...
    
    print_perfect_box(
        title="✅ BACKUP COMPLETADO",
        subtitle="Todos los archivos fueron respaldados",
        description="Ubicación: /backups/2024-01-15.tar.gz",
        width=70,
        color="green"
    )
```

### CLI de Deploy

```bash
#!/usr/bin/env bash
source skills/perfect-boxes/bash/perfect_banner.sh

print_fancy_banner "🚀 DEPLOY SCRIPT" "Producción - v2.1.0" 70

print_header "📦 Construyendo aplicación" "🔨"
npm run build

print_header "🚢 Desplegando a servidor" "🌐"
scp -r dist/ user@server:/var/www/

print_perfect_box "✅ DEPLOY EXITOSO" "La aplicación está en línea" "URL: https://miapp.com" 70 "$COLOR_GREEN"
```

### CLI Interactivo

```python
from perfect_box import print_perfect_box, print_header

def main_menu():
    print_perfect_box(
        title="📋 MENÚ PRINCIPAL",
        subtitle="Selecciona una opción",
        width=60,
        color="cyan"
    )
    
    print("\n  1. Procesar archivos")
    print("  2. Ver estadísticas")
    print("  3. Configuración")
    print("  4. Salir\n")
    
    choice = input("  Opción: ")
    
    if choice == "1":
        print_header("📁 Procesando archivos...", color="yellow")
        # ...
```

---

## Consejos de Rendimiento

1. **Carga lazy:** Solo importa cuando necesites UI:
```python
def show_results():
    from perfect_box import print_perfect_box
    print_perfect_box("Resultados", ...)
```

2. **Cache de funciones:** Si dibujas muchos cuadros, considera cachear:
```python
from functools import lru_cache
from perfect_box import get_visual_width

@lru_cache(maxsize=128)
def cached_width(text):
    return get_visual_width(text)
```

3. **Suprimir output en tests:**
```python
import io
import sys

def test_silent():
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    print_perfect_box("Test")
    
    sys.stdout = old_stdout
```

---

## Recursos Adicionales

- 📖 [README principal](./README.md)
- 🧪 [Tests](./python/test_perfect_box.py)
- 💻 [Demo completa](./demo_app.py)
- 📝 [Ejemplos](./examples/)

---

**¿Preguntas?** Abre un issue o contribuye mejoras a la skill.
