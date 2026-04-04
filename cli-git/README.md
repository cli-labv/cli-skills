# CLI Git 🔀

Smart Git workflow automation with intelligent change analysis.

## Problem

```bash
# Typical frustrating workflow:
$ git status
  borrados: CHANGELOG.md
  borrados: INSTALL.md
  sin seguimiento: docs/

$ git add .
$ git commit -m "cambios"  # 😞 Bad message
$ git push
```

## Solution

```bash
# With cli-git:
$ python -m cli_git commit

╭───────────── 📊 Análisis de Cambios ─────────────╮
│                                                   │
│ 📁 MOVIMIENTOS DETECTADOS                        │
│    CHANGELOG.md → docs/CHANGELOG.md              │
│    INSTALL.md → docs/INSTALL.md                  │
│                                                   │
│ ➕ NUEVOS                                        │
│    docs/README.md                                │
│                                                   │
╰───────────────────────────────────────────────────╯

💡 Mensaje de commit sugerido:
----------------------------------------
refactor: mover archivos a docs/

- Mover CHANGELOG.md → docs/
- Mover INSTALL.md → docs/
- Agregar docs/README.md
----------------------------------------

¿Proceder con el commit? [S/n]
```

## Features

### 1. Smart Move Detection

Git shows `deleted` when a file is moved. cli-git detects this:

```
Git shows:           cli-git shows:
❌ deleted: API.md   📁 API.md → docs/API.md
❌ deleted: run.sh   📁 run.sh → scripts/run.sh
```

### 2. Dangerous Change Alerts

Warns before deleting important files:

```
⚠️ ADVERTENCIA: Eliminaciones peligrosas detectadas:
   - src/main.py (Archivo importante: *.py)
   - requirements.txt (Archivo importante)
```

### 3. Auto Commit Messages

Generates descriptive messages based on changes:

| Changes | Generated Message |
|---------|-------------------|
| Files moved to docs/ | `docs: mover archivos a docs/` |
| Files moved to scripts/ | `chore: mover archivos a scripts/` |
| New test files | `test: agregar tests` |
| Bug fixes | `fix: actualizar archivo.py` |
| Restructure | `refactor: reorganizar proyecto` |

## Installation

```bash
pip install rich  # Optional but recommended
```

## Usage

### Analyze Changes

```python
from skills.cli_git import analyze

analysis = analyze()

# Check results
if analysis.has_dangerous:
    print("¡Cuidado!")

print(f"Moved: {len(analysis.moved)}")
print(f"Added: {len(analysis.added)}")
print(f"Deleted: {len(analysis.deleted)}")
```

### Get Suggested Message

```python
from skills.cli_git import suggest_message

msg = suggest_message()
print(msg)
# Output:
# refactor: reorganizar estructura del proyecto
#
# - Mover CHANGELOG.md → docs/
# - Mover install.sh → scripts/
```

### Smart Commit (Interactive)

```python
from skills.cli_git import smart_commit

# Shows analysis, suggests message, asks confirmation
smart_commit()

# Auto-push after commit
smart_commit(auto_push=True)

# Use custom message
smart_commit(custom_message="feat: nueva funcionalidad")
```

### Quick Push (One-liner)

```python
from skills.cli_git import quick_push

# Auto-generate message and push
quick_push()

# Custom message
quick_push("fix: corregir bug crítico")
```

## CLI Usage

```bash
# Analyze changes
python -m cli_git analyze

# Suggest commit message
python -m cli_git suggest

# Interactive commit
python -m cli_git commit

# Quick push
python -m cli_git push
```

## Configuration

### Dangerous File Patterns

Files matching these patterns trigger warnings when deleted:

```python
DANGEROUS_PATTERNS = [
    "*.py", "*.js", "*.ts",    # Code
    "requirements.txt",         # Dependencies
    "pyproject.toml",
    ".env",                     # Config
    "Dockerfile",
    "README.md",                # Docs
]
```

### Safe to Delete

These files won't trigger warnings:

```python
SAFE_TO_DELETE = [
    "*.pyc",
    "__pycache__/*",
    "*.log",
    "dist/*",
    "build/*",
]
```

## Integration with AI Agents

Add to agent instructions:

```
Before committing changes:
1. Use analyze() to review changes
2. Check analysis.has_dangerous for risky deletions
3. Use suggest_message() for descriptive commits
4. Use smart_commit() for guided workflow
```

## License

MIT
