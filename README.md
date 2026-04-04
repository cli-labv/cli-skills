# Skills Directory 🎯

> **¿Qué es esto?** Un repositorio de **guías y blueprints reutilizables** (skills) para crear aplicaciones CLI profesionales.

> **⚠️ IMPORTANTE:** Las skills son **referencias y patrones**, NO código a instalar en tus proyectos.

---

## 🎯 ¿Qué es una Skill?

Una skill es una **guía de implementación** que:
- ✅ Resuelve un problema común en desarrollo CLI
- ✅ Muestra **CÓMO** resolver el problema (patrón)
- ✅ Incluye documentación clara con ejemplos
- ✅ Es reutilizable: el agente aprende y genera SU PROPIO código
- ✅ Se usa TEMPORALMENTE durante desarrollo, luego se elimina

### La Diferencia:
```
❌ MALO:     "Skill" es un módulo que instalo en mi proyecto
✅ CORRECTO: "Skill" es una guía que consulto, aprendo y elimino
```

---

## 🚀 Quick Start para Agentes IA

```bash
# Tu proyecto durante desarrollo
proyecto/
├─ cli-skills/          ← Skills como REFERENCIA (temporal)
├─ src/                 ← Tu código (permanente)
└─ requirements.txt

# Cuando terminas:
proyecto/
├─ src/                 ← Tu código (completamente independiente)
└─ requirements.txt     ← Solo dependencias reales

# ¿Qué pasó? → cli-skills/ fue eliminado (job done!)
```

**📖 LEER PRIMERO:** [AGENT_GUIDE.md](./AGENT_GUIDE.md) - Guía completa para agentes

---

## 📚 Skills Disponibles (14 Total)

### 1. **perfect-boxes** 📦
**Patrón**: Cálculo de ancho visual de caracteres (emojis = 2 celdas)  
**Lee para aprender**: Cómo manejar emojis en terminal  
**Usa en**: Cuadros, banners, headers  
📁 [Ver documentación](./perfect-boxes/README.md)

```python
# Agente lee perfect-boxes/ y genera:
def create_box(title, width=60):
    # Su PROPIO código basado en el patrón
    visual_width = calculate_visual_width(title)
    # ...
```

### 2. **cli-banners** 🎨
**Patrón**: ASCII art con múltiples estilos + animaciones (typewriter, fade-in, bounce, spinner)  
**Lee para aprender**: Matrices de caracteres, loops, animaciones con time.sleep  
**Usa en**: Títulos, logos, welcome screens  
📁 [Ver documentación](./cli-banners/README.md)

### 3. **cli-prompts** 💬
**Patrón**: Input interactivo bonito con questionary  
**Lee para aprender**: Cómo hacer UX de prompts  
**Usa en**: Confirmaciones, selecciones, passwords  
📁 [Ver documentación](./cli-prompts/README.md)

### 4. **cli-progress** ⏳
**Patrón**: Spinners y progress bars con rich  
**Lee para aprender**: Context managers para animaciones  
**Usa en**: Descargas, builds, procesamiento largo  
📁 [Ver documentación](./cli-progress/README.md)

### 5. **cli-tables** 📊
**Patrón**: Tablas formateadas con ancho visual correcto  
**Lee para aprender**: Formateo con rich.table  
**Usa en**: Listar datos, mostrar resultados  
📁 [Ver documentación](./cli-tables/README.md)

### 6. **cli-args** 🎯
**Patrón**: CLI argument parsing limpio con Typer  
**Lee para aprender**: @app.command() decorator pattern  
**Usa en**: Flags, opciones, subcomandos  
📁 [Ver documentación](./cli-args/README.md)

### 7. **cli-logger** 📝
**Patrón**: Logging bonito con iconos y colores  
**Lee para aprender**: Formateo de logging con rich  
**Usa en**: Debug, info, warnings, errores  
📁 [Ver documentación](./cli-logger/README.md)

### 8. **cli-config** ⚙️
**Patrón**: Configuración multi-formato (JSON, YAML, TOML, .env)  
**Lee para aprender**: Pydantic BaseSettings pattern  
**Usa en**: Configuración de apps, variables de entorno  
📁 [Ver documentación](./cli-config/README.md)

### 9. **cli-errors** ❌
**Patrón**: Mensajes de error bonitos con hints  
**Lee para aprender**: Custom exception formatting  
**Usa en**: Manejo de errores, feedback al usuario  
📁 [Ver documentación](./cli-errors/README.md)

### 10. **cli-wizard** 🧙
**Patrón**: Wizards multi-paso con progreso y validación  
**Lee para aprender**: State machines para configuración  
**Usa en**: Setup inicial, onboarding, configuración guiada  
📁 [Ver documentación](./cli-wizard/README.md)

### 11. **cli-help** 📖
**Patrón**: Auto-generación de help desde docstrings  
**Lee para aprender**: Introspección y generación de UI  
**Usa en**: --help, documentación de comandos  
📁 [Ver documentación](./cli-help/README.md)

### 12. **cli-updater** 🔄
**Patrón**: Detección de nuevas versiones (PyPI, GitHub)  
**Lee para aprender**: Checking remotes, comparison de versiones  
**Usa en**: Version checks, notificaciones de update  
📁 [Ver documentación](./cli-updater/README.md)

### 13. **cli-scaffold** 🏗️
**Patrón**: Validación de estructura de proyecto  
**Lee para aprender**: File placement rules, validation patterns  
**Usa en**: Validar estructura, generar start.sh  
📁 [Ver documentación](./cli-scaffold/README.md)

### 14. **cli-git** 🔧
**Patrón**: Smart git automation (análisis de cambios, sugerencias de commits)  
**Lee para aprender**: Git subprocess, change detection, intelligent naming  
**Usa en**: Automatizar git workflow, commits inteligentes  
📁 [Ver documentación](./cli-git/README.md)


---

## 📋 Cómo Usar las Skills Correctamente

### ✅ FLUJO CORRECTO

```bash
# Fase 1: Exploración (Agente estudia skills)
cd tu-proyecto/
ls cli-skills/          # Ver disponibles
cat cli-skills/cli-banners/README.md    # Leer documentación

# Fase 2: Generación (Agente crea SU CÓDIGO)
# Agente escribe src/my_banner.py basado en el PATRÓN

# Fase 3: Integración (Agente usa su código)
# src/main.py importa de src.my_banner (NO de cli-skills/)

# Fase 4: Limpieza (Agente elimina skills)
rm -rf cli-skills/
git add .
git commit -m "feat: add interactive banners"
git push
```

### ❌ LO QUE NUNCA DEBES HACER

```python
# ❌ MALO - Importar directo de skills
from cli_skills.cli_banners import generate_text

# ✅ BIEN - Tu propio código
from src.banner_generator import generate_text
```

**LEER:** [AGENT_GUIDE.md](./AGENT_GUIDE.md) para instrucciones completas

---

## 🔗 Índices y Documentación

- **[SKILLS_INDEX.md](./SKILLS_INDEX.md)** - Catálogo completo de las 14 skills
- **[AGENT_GUIDE.md](./AGENT_GUIDE.md)** - Guía paso a paso para agentes IA

## 📊 Estructura de una Skill

Cada skill sigue esta estructura estándar:

```
skills/
└── nombre-de-la-skill/
    ├── README.md                      # Documentación completa
    ├── bash/                          # Implementación en Bash
    │   └── script.sh
    ├── python/                        # Implementación en Python
    │   └── module.py
    ├── javascript/                    # Implementación en JS (opcional)
    │   └── module.js
    └── examples/                      # Ejemplos de uso
        ├── example_basic.txt
        └── example_advanced.txt
```

## Cómo Usar las Skills

### ✅ FORMA CORRECTA: Leer, Aprender, Generar, Eliminar
1. Lee el README.md de la skill para entender el PATRÓN
2. Revisa los ejemplos en examples/
3. Genera TU PROPIO código en src/ (basado en el patrón)
4. Tu código es completamente independiente
5. Antes de hacer push: `rm -rf cli-skills/`
6. Verifica que el proyecto funciona SIN cli-skills/

### ❌ FORMA INCORRECTA: Copiar y Pegar
```python
# NO HAGAS ESTO:
cp cli-skills/cli_banners/python/cli_banners.py src/
from src.cli_banners import generate_text  # Depende del patrón

# HAZ ESTO:
# Lee cli_banners.py, entiende el patrón
# Escribe tu propio my_banner.py
from src.my_banner import generate_text  # Tu código
```

---

## 💡 Filosofía de Skills

Las skills NO son:
- ❌ Módulos para instalar en el proyecto
- ❌ Código para copiar-pegar
- ❌ Dependencias en requirements.txt
- ❌ Carpetas que subes a git

Las skills SON:
- ✅ Guías de implementación
- ✅ Blueprints y patrones
- ✅ Referencias de cómo resolver problemas
- ✅ Documentación ejecutable
- ✅ Temporales (durante desarrollo)

---

## Licencia

Todas las skills en este directorio son de dominio público o MIT. Puedes usarlas y aprender de ellas libremente.
