# Skills Directory 🎯

Este directorio contiene **skills reutilizables** que resuelven problemas comunes en desarrollo CLI.

## ¿Qué es una Skill?

Una skill es una colección de funciones, scripts y documentación que:
- ✅ Resuelve un problema específico y común
- ✅ Es reutilizable en múltiples proyectos
- ✅ Incluye documentación clara con ejemplos
- ✅ Tiene versiones en diferentes lenguajes (Bash, Python, etc.)
- ✅ Está lista para copiar y usar

## Skills Disponibles

### 1. **perfect-boxes** 📦
**Problema**: Cuadros Unicode desalineados cuando contienen emojis  
**Solución**: Calcula el ancho visual real de caracteres (emojis = 2 celdas)  
**Idiomas**: Python ✅, Bash ✅  
**Uso**: Banners, cuadros, headers en CLI  
📁 [Ver documentación](./perfect-boxes/README.md)

```python
from skills.perfect_boxes.python.perfect_box import print_perfect_box
print_perfect_box("📸 MI APP 📄", "Subtítulo", width=60)
```

### 2. **cli-banners** 🎨
**Problema**: Generar ASCII art profesional sin herramientas externas  
**Solución**: Generador integrado de texto y símbolos ASCII con colores  
**Idiomas**: Python ✅, Bash ✅  
**Uso**: Títulos, logos, íconos, menús interactivos  
📁 [Ver documentación](./cli-banners/README.md)

### 3. **cli-prompts** 💬
**Problema**: Input interactivo feo y repetitivo  
**Solución**: Prompts bonitos con colores, validación y navegación  
**Idiomas**: Python ✅  
**Uso**: Confirmaciones, selecciones, passwords, números  
📁 [Ver documentación](./cli-prompts/README.md)

### 4. **cli-progress** ⏳
**Problema**: Sin feedback visual durante operaciones largas  
**Solución**: Spinners animados y barras de progreso configurables  
**Idiomas**: Python ✅  
**Uso**: Descargas, builds, procesamiento de archivos  
📁 [Ver documentación](./cli-progress/README.md)

### 5. **cli-tables** 📊
**Problema**: Tablas desalineadas, especialmente con emojis  
**Solución**: Tablas formateadas con 6 estilos y manejo de ancho visual  
**Idiomas**: Python ✅  
**Uso**: Listar datos, mostrar resultados, key-value pairs  
📁 [Ver documentación](./cli-tables/README.md)

### 6. **cli-args** 🎯
**Problema**: argparse es verboso y tedioso  
**Solución**: API limpia para parsing de argumentos con help bonito  
**Idiomas**: Python ✅  
**Uso**: Flags, opciones, subcomandos  
📁 [Ver documentación](./cli-args/README.md)

### 7. **cli-logger** 📝
**Problema**: Logging feo y sin colores  
**Solución**: Logger bonito con iconos, colores y niveles claros  
**Idiomas**: Python ✅  
**Uso**: Debug, info, warnings, errores, timing  
📁 [Ver documentación](./cli-logger/README.md)

### 8. **cli-config** ⚙️
**Problema**: Manejar múltiples formatos de config es tedioso  
**Solución**: Gestor unificado para JSON, YAML, TOML, .env  
**Idiomas**: Python ✅  
**Uso**: Configuración de apps, variables de entorno  
📁 [Ver documentación](./cli-config/README.md)

### 9. **cli-errors** ❌
**Problema**: Errores feos e inútiles  
**Solución**: Mensajes de error bonitos con hints y sugerencias  
**Idiomas**: Python ✅  
**Uso**: Manejo de errores, mensajes para usuarios  
📁 [Ver documentación](./cli-errors/README.md)

### 10. **cli-wizard** 🧙
**Problema**: Configuración inicial tedios  
**Solución**: Wizards multi-paso con progreso y validación  
**Idiomas**: Python ✅  
**Uso**: Setup inicial, onboarding, configuración guiada  
📁 [Ver documentación](./cli-wizard/README.md)

### 11. **cli-help** 📖
**Problema**: Help text desincronizado y feo  
**Solución**: Generación automática desde docstrings y signatures  
**Idiomas**: Python ✅  
**Uso**: --help, documentación de comandos  
📁 [Ver documentación](./cli-help/README.md)

### 12. **cli-updater** 🔄
**Problema**: Usuarios sin saber de nuevas versiones  
**Solución**: Verificación automática con notificaciones bonitas  
**Idiomas**: Python ✅  
**Uso**: GitHub, PyPI, npm version checks  
📁 [Ver documentación](./cli-updater/README.md)

---

## Estructura de una Skill

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

### Opción 1: Importar directamente
```python
# Python
from skills.perfect_boxes.python.perfect_box import print_perfect_box

# Bash
source skills/perfect-boxes/bash/perfect_banner.sh
```

### Opción 2: Copiar a tu proyecto
Copia la carpeta de la skill a tu proyecto y úsala localmente.

### Opción 3: Instalar como paquete
Algunas skills pueden empaquetarse como módulos instalables.

## Contribuir una Nueva Skill

¿Tienes una solución reutilizable? Agrégala aquí:

1. Crea una carpeta con el nombre descriptivo (kebab-case)
2. Sigue la estructura estándar (README, bash/, python/, examples/)
3. Documenta el problema que resuelve
4. Incluye ejemplos claros de uso
5. Actualiza este README con tu skill

## Licencia

Todas las skills en este directorio son de dominio público o MIT. Puedes usarlas libremente en tus proyectos.
