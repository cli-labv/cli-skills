# 🎯 CLI-Skills Library - Complete Index

> **¿Qué es esto?** Un repositorio de **guías de implementación reutilizables** (skills) para crear aplicaciones CLI profesionales.

> **⚠️ IMPORTANTE:** Estas skills son **referencias y blueprints**, NO código a copiar-pegar al proyecto final.

---

## 📌 ¿Cómo Usar Esta Librería?

### Para Agentes IA:
```
1. Consulta la skill que necesitas (ej: cli-banners/)
2. Lee su README.md para entender el patrón
3. Estudia los ejemplos en examples/
4. Genera TU PROPIO código optimizado para el proyecto
5. Elimina la carpeta cli-skills/ antes de hacer push
```

### Ciclo de Vida de Skills en un Proyecto:
```
Durante desarrollo:
proyecto/
├─ cli-skills/         ← Skills como REFERENCIA
├─ src/               ← Tu código generado
└─ requirements.txt

Antes de push:
proyecto/
├─ src/               ← Tu código (INDEPENDIENTE)
└─ requirements.txt   ← Solo dependencias reales

❌ cli-skills/ fue ELIMINADO (job done!)
```

---

## 📚 **SKILL CATALOG (14 Skills)**

### **🎨 UI & Display (6 Skills)**

| Skill | Propósito | Nivel | Ejemplo |
|-------|-----------|-------|---------|
| **[cli-banners](./cli-banners/)** | Generar ASCII art, banners, con animaciones (typewriter, fade-in, bounce, spinner) | ⭐⭐ | `generate_text("HELLO", style="block", animate="typewriter")` |
| **[perfect-boxes](./perfect-boxes/)** | Cuadros perfectos en terminal con soporte para emojis de ancho doble | ⭐ | `print_perfect_box("Content", icon="📸", width=60)` |
| **[cli-tables](./cli-tables/)** | Tablas formateadas con colores, sorting, borders | ⭐⭐ | `print_table([{"name": "Alice"}, ...], color="cyan")` |
| **[cli-progress](./cli-progress/)** | Progress bars, spinners, indeterminate progress con rich | ⭐⭐ | `with spinner("Processing..."): do_work()` |
| **[cli-help](./cli-help/)** | Auto-generación de ayuda bonita con panels y ejemplos | ⭐⭐ | `show_help({"command": "deploy", "examples": [...]})` |
| **[cli-logger](./cli-logger/)** | Logging con iconos (✅ ❌ ⚠️ ℹ️) y colores por nivel | ⭐ | `logger.success("Deploy complete")` |

### **💬 Input & Interaction (3 Skills)**

| Skill | Propósito | Nivel | Ejemplo |
|-------|-----------|-------|---------|
| **[cli-prompts](./cli-prompts/)** | Prompts interactivos (select, confirm, input, password) con questionary | ⭐ | `select("Choose:", choices=[...])` |
| **[cli-wizard](./cli-wizard/)** | Multi-step configuration wizard con progreso y validación | ⭐⭐ | `wizard.add_step("name", type="text").run()` |
| **[cli-args](./cli-args/)** | Argument parsing con Typer - más simple que argparse | ⭐ | `@app.command()` decorator |

### **⚙️ Configuration & State (3 Skills)**

| Skill | Propósito | Nivel | Ejemplo |
|-------|-----------|-------|---------|
| **[cli-config](./cli-config/)** | Config multi-format (JSON, YAML, TOML, .env) con Pydantic | ⭐⭐ | `config.database.host` |
| **[cli-scaffold](./cli-scaffold/)** | Validación de estructura de proyecto y generación de start.sh | ⭐⭐ | `validate_project_structure()` |
| **[cli-git](./cli-git/)** | Smart git workflow - analiza cambios, sugiere commits, detecta movimientos | ⭐⭐ | `analyzer.suggest_message()` |

### **🚀 Utilities & Tools (2 Skills)**

| Skill | Propósito | Nivel | Ejemplo |
|-------|-----------|-------|---------|
| **[cli-errors](./cli-errors/)** | Beautiful error messages con hints y sugerencias | ⭐ | `@pretty_error("Failed to connect")` |
| **[cli-updater](./cli-updater/)** | Detecta nuevas versiones en PyPI/GitHub, notifica al usuario | ⭐⭐ | `check_for_updates(current_v="1.0.0")` |

---

## 🚀 **Quick Reference**

### Para Crear un CLI Básico:
```python
# Skill: cli-prompts + cli-args
from cli_prompts import select, confirm
from cli_args import app

@app.command()
def main(name: str):
    style = select("Choose style:", choices=["block", "slim"])
    proceed = confirm("Continue?")
```

### Para UI Profesional:
```python
# Skills: cli-banners + cli-progress + cli-tables
from cli_banners import interactive_banner, animate_typewriter
from cli_progress import spinner
from cli_tables import print_table

interactive_banner("MYAPP")  # User picks style/color/animation
with spinner("Loading data..."):
    data = fetch_data()
print_table(data, color="cyan")
```

### Para Configuración y Validación:
```python
# Skills: cli-config + cli-scaffold
from cli_config import Config
from cli_scaffold import validate_structure

config = Config.from_file("config.yaml")
validate_structure()  # Checks project structure
```

### Para Workflow Git Automático:
```python
# Skill: cli-git
from cli_git import GitAnalyzer

analyzer = GitAnalyzer(".")
changes = analyzer.analyze()
message = analyzer.suggest_message()
analyzer.smart_commit(message)
```

---

## 📖 **Skill Details & Documentation**

### By Category:

#### **Display Skills** (Cómo mostrar información bonita)
- [cli-banners](./cli-banners/README.md) - ASCII art & animations
- [perfect-boxes](./perfect-boxes/README.md) - Cuadros con emojis
- [cli-tables](./cli-tables/README.md) - Tablas formateadas
- [cli-progress](./cli-progress/README.md) - Progreso y spinners
- [cli-help](./cli-help/README.md) - Ayuda automática
- [cli-logger](./cli-logger/README.md) - Logging bonito

#### **Input Skills** (Cómo pedir información al usuario)
- [cli-prompts](./cli-prompts/README.md) - Prompts interactivos
- [cli-wizard](./cli-wizard/README.md) - Wizards multi-paso
- [cli-args](./cli-args/README.md) - Argument parsing

#### **Config Skills** (Cómo manejar configuración)
- [cli-config](./cli-config/README.md) - YAML/JSON/TOML
- [cli-scaffold](./cli-scaffold/README.md) - Estructura de proyecto
- [cli-git](./cli-git/README.md) - Git automation

#### **Utility Skills** (Herramientas auxiliares)
- [cli-errors](./cli-errors/README.md) - Error handling bonito
- [cli-updater](./cli-updater/README.md) - Version checking

---

## 🎓 **Learning Path**

### Nivel 1: Fundamentos
1. **cli-banners** - Aprende a mostrar texto bonito
2. **cli-prompts** - Aprende a pedir input
3. **cli-logger** - Aprende a mostrar estado

### Nivel 2: Intermedio
4. **cli-args** - Estructura argumentos
5. **cli-config** - Maneja configuración
6. **cli-tables** - Muestra datos estructurados

### Nivel 3: Avanzado
7. **cli-wizard** - Flujos multi-paso
8. **cli-progress** - Animaciones y progreso
9. **cli-scaffold** - Valida estructura
10. **cli-git** - Automatiza git

---

## 📊 **Tech Stack Used**

| Librería | Skills que la usan | Razón |
|----------|-------------------|-------|
| **rich** | progress, tables, logger, banners | Mejor soporte ANSI colors |
| **questionary** | prompts, wizard, banners (interactive) | UX superior |
| **typer** | args | CLI framework moderno |
| **pydantic** | config | Validación fuerte |
| **pyyaml/tomli** | config | Multi-format support |

---

## 🔍 **How to Navigate This Repo**

```
skills/
├─ cli-banners/
│  ├─ README.md          ← START HERE - Explicación + ejemplos
│  ├─ __init__.py        ← Imports
│  ├─ python/
│  │  ├─ cli_banners.py  ← Código de referencia
│  │  └─ alphabet.py     ← Caracteres disponibles
│  └─ examples/
│     └─ *.py            ← Casos de uso reales
│
├─ cli-prompts/
│  ├─ README.md
│  ├─ core.py
│  └─ examples/
│
├─ ... (más skills)
│
└─ SKILLS_INDEX.md       ← Estás aquí (índice maestro)
```

---

## ✅ **Checklist: Agente IA debe hacer**

Cuando uses skills en un proyecto:

- [ ] Lee el README.md de la skill
- [ ] Entiende el patrón/diseño
- [ ] Revisa los ejemplos en examples/
- [ ] Genera TU PROPIO código en src/ (INDEPENDIENTE)
- [ ] Tu código importa de librerías, NO de skills/
- [ ] Añade verdaderas dependencias a requirements.txt
- [ ] Elimina carpeta `cli-skills/` antes de push
- [ ] Verifica que el proyecto funciona sin skills/
- [ ] Haz commit limpio sin referencias a skills/

---

## 🎯 **Exemplos: Skill como Guía**

### ❌ MAL (Copiar la skill):
```python
# src/main.py
from cli_skills.cli_banners import generate_text
# ← ¡INCORRECTO! Depende de cli_skills que se elimina
```

### ✅ BIEN (Aprender de la skill):
```python
# src/banner_generator.py
# Basado en patrón de cli-banners/python/cli_banners.py
# Pero COMPLETAMENTE INDEPENDIENTE

def generate_ascii_banner(text, style='block'):
    """Tu propia implementación del patrón"""
    # ... tu código aquí ...
    return banner

# src/main.py
from banner_generator import generate_ascii_banner
# ← ✅ CORRECTO! Código propio, sin dependencias de skills/
```

---

## 📝 **Para Contribuir o Mejorar**

Cada skill debe:
1. ✅ Tener un README.md claro
2. ✅ Incluir docstrings en el código
3. ✅ Tener carpeta examples/ con casos reales
4. ✅ Ser completamente independiente
5. ✅ Documentar dependencias externas (rich, questionary, etc.)

---

## 📌 **Resumen Ejecutivo**

> **Las skills son:** Blueprints + Guías + Referencia
> 
> **NO son:** Dependencias + Código a copiar + Módulos del proyecto
> 
> **Ciclo:** Agente lee → Agente aprende → Agente genera → Agente elimina skills/
> 
> **Resultado:** Código limpio, sin contaminación, completamente independiente

---

**Last Updated:** 2026-04-03  
**Total Skills:** 14  
**Lines of Reusable Code:** ~15,000+  
**Status:** 🟢 Production Ready

