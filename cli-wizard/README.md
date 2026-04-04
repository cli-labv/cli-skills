# CLI Wizard 🧙

Multi-step configuration wizards for Python CLI applications.

## Installation

```bash
pip install questionary rich
```

## Quick Start

```python
from skills.cli_wizard import Wizard

wizard = Wizard("Project Setup")
wizard.add_text("name", "Project name:")
wizard.add_select("type", "Type:", ["web", "cli", "api"])
wizard.add_confirm("typescript", "TypeScript?", default=True)

result = wizard.run()

if result.completed:
    print(f"Creating {result['type']} project: {result['name']}")
```

## Features

### Step Types

```python
wizard.add_text("name", "Name:", default="my-app")
wizard.add_password("api_key", "API Key:")
wizard.add_select("db", "Database:", ["postgres", "mysql", "sqlite"])
wizard.add_checkbox("features", "Features:", ["auth", "api", "docs"])
wizard.add_confirm("proceed", "Continue?", default=True)
```

### Conditional Steps

```python
wizard.add_select("type", "Type:", ["web", "cli"])
wizard.add_conditional(
    "framework",
    "Framework:",
    condition=lambda d: d.get("type") == "web",
    type="select",
    choices=["fastapi", "flask", "django"]
)
```

### Result

```python
result = wizard.run()

if result.completed:
    data = result.to_dict()
    name = result["name"]
    name = result.get("name", "default")
```

## License

MIT
