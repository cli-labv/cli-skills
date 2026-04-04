# CLI Config ⚙️

Configuration management for Python CLI applications.

Supports JSON, YAML, TOML, and .env files with dot notation access.

## Installation

```bash
pip install pyyaml  # For YAML support
pip install tomli   # For TOML support (Python < 3.11)
```

## Quick Start

```python
from skills.cli_config import Config

config = Config("myapp")
config.load("config.json")
config.load_env(".env")

db_host = config.get("database.host", "localhost")
db_port = config.get("database.port", 5432, type=int)
```

## Features

### Multiple Formats

```python
config.load("config.json")   # JSON
config.load("config.yaml")   # YAML
config.load("config.toml")   # TOML
config.load_env(".env")      # Environment file
```

### Dot Notation

```python
# config.json:
# {"database": {"host": "localhost", "port": 5432}}

config.get("database.host")  # "localhost"
config.get("database.port")  # 5432
```

### Type Casting

```python
config.get("port", type=int)
config.get("debug", type=bool)
config.get("timeout", type=float)
```

### Environment Override

```python
# Automatically checks MYAPP_DATABASE_HOST
config = Config("myapp")
host = config.get("database.host")
```

### Require Keys

```python
config.require("database.host", "api_key")
```

## API

```python
Config(app_name, env_prefix=None, auto_env=True)
config.load(path, required=False)
config.load_env(path=".env")
config.get(key, default=None, type=None)
config.set(key, value)
config.require(*keys)
config.to_dict()
```

## License

MIT
