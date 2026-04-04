# 🤖 GUÍA PARA AGENTES IA - Uso Correcto de Skills

> Este documento explica **EXACTAMENTE** cómo los agentes deben usar las skills para proyectos CLI.

---

## 🎯 La Mentalidad Correcta

### ❌ INCORRECTO: "Las skills son librerías que instalo"
```
Agente piensa: "Necesito banners, voy a copiar cli-banners/ a mi proyecto"
Resultado: proyecto contaminated con code que no es suyo
```

### ✅ CORRECTO: "Las skills son PATRONES que estudio"
```
Agente piensa: "Necesito banners, voy a leer cómo lo hace cli-banners/, 
               luego implemento MI versión optimizada"
Resultado: código limpio, independiente, optimizado
```

---

## 📋 Workflow Paso a Paso

### Fase 1: Exploración (Agente revisa skills)
```bash
cd proyecto/
ls cli-skills/              # Ver skills disponibles
cat cli-skills/cli-banners/README.md    # Leer documentación
head -20 cli-skills/cli-banners/python/cli_banners.py  # Ver código
cat cli-skills/cli-banners/examples/03_interactive_banner.py  # Ver ejemplos
```

**Salida esperada:** "Ah, entiendo cómo funcionan los banners"

### Fase 2: Generación (Agente crea su propio código)
```python
# src/my_banner_generator.py - BASADO EN el patrón, pero PROPIO

import time
import sys

def generate_ascii_text(text: str, style: str = "block") -> str:
    """
    Mi propia implementación de generador de banners
    
    Aprendí de cli-banners pero esto es completamente mío
    """
    # Mi código aquí, optimizado para MI proyecto
    fonts = {
        'block': {...},  # Definición de fuentes
        'simple': {...}
    }
    # Implementación completa...
    return result


def animate_banner(text: str, animation: str = "none"):
    """Mi propia función de animación"""
    if animation == "typewriter":
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
    # ...
```

### Fase 3: Integración (Agente usa SU código)
```python
# src/main.py

from my_banner_generator import generate_ascii_text, animate_banner

def main():
    banner = generate_ascii_text("MYAPP", style="block")
    animate_banner(banner, animation="typewriter")
    # ...

if __name__ == "__main__":
    main()
```

### Fase 4: Limpieza (Agente elimina skills)
```bash
# Antes de hacer commit:
rm -rf cli-skills/
ls  # Verificar que se fue

# Ahora sí el proyecto está limpio
git add .
git commit -m "feat: add interactive banner generation"
git push
```

---

## 📊 Checklist de Validación

Antes de hacer push, agente debe verificar:

- [ ] **Ningún import de cli-skills**
  ```bash
  grep -r "from cli_skills" src/
  grep -r "import cli_skills" src/
  # Debe retornar 0 coincidencias
  ```

- [ ] **cli-skills/ está eliminado**
  ```bash
  ls -la cli-skills/
  # Debe dar "No such file or directory"
  ```

- [ ] **requirements.txt no tiene paths locales**
  ```bash
  cat requirements.txt
  # No debe haber: ./cli-skills, ../skills, etc.
  ```

- [ ] **El proyecto funciona standalone**
  ```bash
  # Simular ambiente limpio
  python -c "import src.main; src.main.run()"
  # Debe funcionar sin cli-skills/
  ```

- [ ] **Git status está limpio**
  ```bash
  git status
  # Debe mostrar files agregados, nada de "deleted" o "renamed"
  ```

---

## 🎓 Patrones por Categoría

### 🎨 Display Pattern (Banners, Tables, Logging)

```python
# PATRÓN DE SKILL
# cli-banners/python/cli_banners.py:
class BannerGenerator:
    def __init__(self, style='block'):
        self.fonts = {...}
    
    def generate(self, text):
        return self._render(text)


# AGENTE GENERA
# src/ui/banner.py:
class AppBanner:
    """Mi implementación optimizada para storm-dl"""
    def __init__(self, width=60):
        self.width = width
        self.chars = {...}  # Solo lo que necesito
    
    def create_header(self, title):
        """Método específico para mi app"""
        # ...


# AGENTE USA
# src/main.py:
from ui.banner import AppBanner
banner = AppBanner(width=70)
print(banner.create_header("WELCOME"))
```

### 💬 Input Pattern (Prompts, Wizard)

```python
# PATRÓN DE SKILL
# cli-prompts/core.py:
def select(message, choices):
    # Usa questionary internamente
    return questionary.select(message, choices=choices).ask()


# AGENTE GENERA
# src/user_input.py:
def ask_deployment_options():
    """Mi propia función de input para deployment"""
    # Podría usar questionary directamente
    # O implementar algo más simple
    environment = input("Environment [dev]: ") or "dev"
    confirm = input(f"Deploy to {environment}? [y/N]: ")
    return environment if confirm.lower() == 'y' else None


# AGENTE USA
# src/main.py:
from user_input import ask_deployment_options
env = ask_deployment_options()
```

### ⚙️ Config Pattern (Configuration Management)

```python
# PATRÓN DE SKILL
# cli-config/core.py:
from pydantic import BaseSettings
class Config(BaseSettings):
    database_url: str
    api_key: str
    class Config:
        env_file = ".env"


# AGENTE GENERA
# src/config.py:
from pydantic_settings import BaseSettings
class StormConfig(BaseSettings):
    """Mi configuración para storm-dl"""
    input_dir: str
    output_dir: str
    quality: str = "high"
    
    class Config:
        env_file = ".env"


# AGENTE USA
# src/main.py:
from config import StormConfig
config = StormConfig()
process_videos(config.input_dir, config.output_dir)
```

---

## 🚨 Errores Comunes a Evitar

### ❌ Error 1: Copiar archivos de skills
```python
# MALO:
cp cli-skills/cli_banners/python/*.py src/
# El proyecto ahora depende de skills/ que será eliminado

# BIEN:
# Leer cli_banners.py, aprender el patrón
# Escribir my_banner.py con MI implementación
```

### ❌ Error 2: Importar directamente de skills
```python
# MALO:
from cli_skills.cli_banners import generate_text

# BIEN:
from src.banner_generator import generate_text
```

### ❌ Error 3: Dejar cli-skills/ en el proyecto final
```bash
# MALO:
git add cli-skills/
git commit -m "Add features"
git push

# BIEN:
rm -rf cli-skills/
git add src/
git commit -m "Add features"
git push
```

### ❌ Error 4: No eliminar imports de skills
```python
# MALO - Agente olvida actualizar imports:
# src/main.py sigue importando de cli_skills/

# BIEN:
# src/main.py importa de src/ solamente
```

---

## ✅ Validación Final

Antes de considerar el trabajo "done", agente debe ejecutar:

```bash
# 1. Verificar no hay referencias a skills
grep -r "cli-skills" . 2>/dev/null | wc -l
# Debe retornar 0

# 2. Verificar cli-skills no existe
test -d cli-skills && echo "ERROR: cli-skills aún existe" || echo "OK: Eliminado"

# 3. Correr el proyecto sin skills/
python src/main.py
# Debe funcionar perfectamente

# 4. Ver git status limpio
git status --short
# Solo debe mostrar M (modificados) y A (agregados), 
# pero NO referencias a skills/

# 5. Ver que requirements.txt tiene solo dependencias reales
cat requirements.txt
# Debe tener: rich, questionary, pydantic, etc.
# NO debe tener: ./cli-skills, ../skills, etc.
```

---

## 📚 Referencias Rápidas

### Tabla de Skills y qué aprender:

| Cuando necesites... | Skill a Leer | Patrón a Aprender |
|-------------------|--------------|-------------------|
| Mostrar banners | [cli-banners](../cli-banners/README.md) | Matrices de caracteres + loops |
| Pedir input | [cli-prompts](../cli-prompts/README.md) | Cómo wrapper questionary |
| Mostrar tabla | [cli-tables](../cli-tables/README.md) | Formateo con rich |
| Progreso | [cli-progress](../cli-progress/README.md) | Context managers |
| Config | [cli-config](../cli-config/README.md) | Pydantic BaseSettings |
| Validar estructura | [cli-scaffold](../cli-scaffold/README.md) | Path checking + validation |
| Automatizar git | [cli-git](../cli-git/README.md) | Git subprocess + análisis |

---

## 🎯 TL;DR (Resumen Ejecutivo)

```
AGENTE WORKFLOW:

1. Lee      → Abre README.md de skill
2. Aprende  → Entiende el patrón
3. Genera   → Escribe código PROPIO en src/
4. Prueba   → Verifica funciona sin skills/
5. Limpia   → rm -rf cli-skills/
6. Sube     → git push (proyecto limpio)

NUNCA:
❌ Copiar archivos de skills/ al proyecto
❌ Importar de cli_skills/ en el código final
❌ Dejar cli-skills/ en el commit final
❌ Listar cli-skills/ en requirements.txt
```

---

**Versión:** 1.0  
**Última actualización:** 2026-04-04  
**Para:** Agentes IA y Desarrolladores
