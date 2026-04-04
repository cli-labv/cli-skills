# CLI Scaffold 📁

Project structure validation and shell script orchestration.

## Purpose

Solve two common problems:

1. **Files in wrong places** - Agents creating `.md` files in root instead of `docs/`
2. **Too many shell scripts** - Multiple `.sh` files cluttering the project

## Installation

No dependencies required (pure Python).

## Quick Start

### 1. Validate File Paths

```python
from skills.cli_scaffold import validate_path, get_correct_path

# Check if path is correct
valid, suggestion = validate_path("CHANGELOG.md")
# valid=False, suggestion="docs/CHANGELOG.md"

# Get correct path directly
path = get_correct_path("install.sh")
# Returns: "scripts/install.sh"

# Some files ARE allowed in root
path = get_correct_path("README.md")
# Returns: "README.md" (allowed in root)
```

### 2. Generate Consolidated start.sh

Instead of having multiple scripts:
```
❌ install.sh
❌ setup.sh  
❌ run.sh
❌ build.sh
❌ test.sh
```

Generate ONE `start.sh` that does everything:
```
✅ start.sh install
✅ start.sh run
✅ start.sh build
✅ start.sh test
```

```python
from skills.cli_scaffold import generate_start_sh

sh_content = generate_start_sh(
    project_name="myapp",
    python_cmd="python3",
    use_venv=True,
    main_script="src/main.py"
)

# Write to file
with open("start.sh", "w") as f:
    f.write(sh_content)
```

### 3. Scaffold New Project

```python
from skills.cli_scaffold import scaffold_project

# Create complete project structure
files = scaffold_project("myapp", template="python-cli")

# Creates:
# myapp/
# ├── README.md
# ├── start.sh          # Single entry point
# ├── requirements.txt
# ├── .gitignore
# ├── src/
# │   ├── __init__.py
# │   └── main.py
# ├── tests/
# │   ├── __init__.py
# │   └── test_main.py
# ├── docs/
# └── scripts/
```

## File Placement Rules

### Allowed in Root
- `README.md`
- `LICENSE`
- `.gitignore`
- `requirements.txt`
- `pyproject.toml`
- `setup.py`
- `Makefile`
- `Dockerfile`
- `docker-compose.yml`
- `start.sh` (the ONE script)
- `package.json`

### Must Go in Folders

| File Pattern | Correct Location |
|-------------|------------------|
| `*.md` (except README) | `docs/` |
| `CHANGELOG*` | `docs/` |
| `CONTRIBUTING*` | `docs/` |
| `*.sh` (except start.sh) | `scripts/` |
| `install*.sh` | `scripts/` |
| `test_*.py` | `tests/` |
| `*_test.py` | `tests/` |
| `conftest.py` | `tests/` |

## start.sh Commands

The generated `start.sh` includes:

```bash
./start.sh install   # Install dependencies
./start.sh run       # Run application
./start.sh dev       # Development mode
./start.sh test      # Run tests
./start.sh lint      # Run linter
./start.sh build     # Build project
./start.sh clean     # Clean temp files
./start.sh help      # Show help
```

## Design Principles

The generated scripts follow **SOLID**:

- **Single Responsibility**: Each `cmd_*` function does ONE thing
- **Open/Closed**: Easy to add new commands without modifying existing ones
- **DRY**: Common logic (logging, venv) in shared functions

## Custom Rules

```python
from skills.cli_scaffold import ProjectRules, validate_path

# Create custom rules
rules = ProjectRules()
rules.root_allowed.add("CUSTOM_FILE.txt")  # Allow in root
rules.extension_rules[".config"] = "config"  # .config files → config/

# Use custom rules
valid, suggestion = validate_path("myfile.config", rules)
```

## Integration with AI Agents

Add to your agent's system prompt:

```
Before creating any file, validate the path:
- Use get_correct_path() to get the proper location
- .md files (except README.md) go in docs/
- .sh files (except start.sh) go in scripts/
- test files go in tests/
```

## License

MIT
