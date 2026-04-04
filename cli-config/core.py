"""
Core implementation of CLI Config.

Configuration management with support for JSON, YAML, TOML, and env files.
"""

from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

T = TypeVar("T")


class Config:
    """
    Configuration manager supporting multiple file formats.
    
    Example:
        >>> config = Config("myapp")
        >>> config.load("config.json")
        >>> config.load_env(".env")
        >>> 
        >>> host = config.get("database.host", "localhost")
        >>> port = config.get("database.port", 5432, type=int)
    """
    
    def __init__(
        self,
        app_name: str = "app",
        env_prefix: Optional[str] = None,
        auto_env: bool = True,
    ):
        """
        Initialize config manager.
        
        Args:
            app_name: Application name
            env_prefix: Prefix for env vars (default: APP_NAME_)
            auto_env: Auto-check environment variables
        """
        self.app_name = app_name
        self.env_prefix = env_prefix or f"{app_name.upper()}_"
        self.auto_env = auto_env
        self._data: Dict[str, Any] = {}
    
    def load(
        self,
        path: Union[str, Path],
        required: bool = False,
    ) -> "Config":
        """
        Load configuration from file.
        
        Args:
            path: Path to config file
            required: Raise error if not found
        
        Returns:
            Self for chaining
        """
        path = Path(path).expanduser()
        
        if not path.exists():
            if required:
                raise FileNotFoundError(f"Config not found: {path}")
            return self
        
        # Detect format and load
        suffix = path.suffix.lower()
        
        if suffix == ".json":
            data = self._load_json(path)
        elif suffix in (".yaml", ".yml"):
            data = self._load_yaml(path)
        elif suffix == ".toml":
            data = self._load_toml(path)
        elif suffix == ".env" or path.name == ".env":
            data = self._load_env_file(path)
        else:
            data = self._load_json(path)  # Default to JSON
        
        self._merge(self._data, data)
        return self
    
    def _load_json(self, path: Path) -> Dict[str, Any]:
        with open(path) as f:
            return json.load(f)
    
    def _load_yaml(self, path: Path) -> Dict[str, Any]:
        try:
            import yaml
            with open(path) as f:
                return yaml.safe_load(f) or {}
        except ImportError:
            raise ImportError("pyyaml required: pip install pyyaml")
    
    def _load_toml(self, path: Path) -> Dict[str, Any]:
        try:
            import tomllib
            with open(path, "rb") as f:
                return tomllib.load(f)
        except ImportError:
            try:
                import tomli
                with open(path, "rb") as f:
                    return tomli.load(f)
            except ImportError:
                raise ImportError("tomli required: pip install tomli")
    
    def _load_env_file(self, path: Path) -> Dict[str, Any]:
        data = {}
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    data[key] = value
                    os.environ.setdefault(key, value)
        return data
    
    def load_env(self, path: Union[str, Path] = ".env") -> "Config":
        """Load .env file."""
        return self.load(path, required=False)
    
    def _merge(self, base: Dict, overlay: Dict) -> None:
        """Deep merge overlay into base."""
        for key, value in overlay.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge(base[key], value)
            else:
                base[key] = value
    
    def get(
        self,
        key: str,
        default: T = None,
        type: Optional[Type[T]] = None,
    ) -> T:
        """
        Get configuration value.
        
        Args:
            key: Config key (dot notation: "database.host")
            default: Default value
            type: Type to cast to
        
        Returns:
            Configuration value
        """
        # Check environment first
        if self.auto_env:
            env_key = f"{self.env_prefix}{key.upper().replace('.', '_')}"
            env_val = os.environ.get(env_key)
            if env_val is not None:
                return self._cast(env_val, type)
        
        # Navigate nested keys
        value = self._data
        for part in key.split("."):
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        
        return self._cast(value, type) if type else value
    
    def _cast(self, value: Any, type: Optional[Type[T]]) -> T:
        """Cast value to type."""
        if type is None:
            return value
        if type == bool:
            if isinstance(value, bool):
                return value
            return str(value).lower() in ("true", "1", "yes", "on")
        return type(value)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        parts = key.split(".")
        data = self._data
        for part in parts[:-1]:
            data = data.setdefault(part, {})
        data[parts[-1]] = value
    
    def require(self, *keys: str) -> "Config":
        """Require keys exist."""
        missing = [k for k in keys if self.get(k) is None]
        if missing:
            raise ValueError(f"Missing config: {', '.join(missing)}")
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """Get all config as dict."""
        return dict(self._data)
    
    def __getitem__(self, key: str) -> Any:
        return self.get(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)
    
    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None


def load(path: Union[str, Path], **kwargs) -> Config:
    """Quick load a config file."""
    config = Config(**kwargs)
    config.load(path, required=True)
    return config


def load_env(path: str = ".env", **kwargs) -> Config:
    """Quick load .env file."""
    config = Config(**kwargs)
    config.load_env(path)
    return config


if __name__ == "__main__":
    import tempfile
    
    print("CLI Config Demo")
    print("=" * 40)
    
    # Create temp config
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({
            "app": {"name": "Demo", "version": "1.0"},
            "database": {"host": "localhost", "port": 5432},
        }, f)
        config_path = f.name
    
    config = Config("demo")
    config.load(config_path)
    
    print(f"App name: {config.get('app.name')}")
    print(f"DB host: {config.get('database.host')}")
    print(f"DB port: {config.get('database.port', type=int)}")
    print(f"Missing: {config.get('missing', 'default')}")
    
    os.unlink(config_path)
