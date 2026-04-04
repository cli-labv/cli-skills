"""
Core implementation of CLI Logger.

Beautiful logging with rich formatting.
"""

from __future__ import annotations

import sys
import logging
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Any, Optional
from contextlib import contextmanager
import time

try:
    from rich.console import Console
    from rich.text import Text
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


class LogLevel(IntEnum):
    """Log levels."""
    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


@dataclass
class LogStyle:
    """Log level styling."""
    icon: str
    color: str


STYLES = {
    LogLevel.TRACE: LogStyle("🔬", "dim"),
    LogLevel.DEBUG: LogStyle("🐛", "dim cyan"),
    LogLevel.INFO: LogStyle("ℹ️ ", "blue"),
    LogLevel.SUCCESS: LogStyle("✅", "green"),
    LogLevel.WARNING: LogStyle("⚠️ ", "yellow"),
    LogLevel.ERROR: LogStyle("❌", "red"),
    LogLevel.CRITICAL: LogStyle("💥", "bold red"),
}


class Logger:
    """
    Beautiful CLI logger.
    
    Example:
        >>> log = Logger()
        >>> log.info("Starting process")
        >>> log.success("Done!")
        >>> log.error("Something failed")
    """
    
    def __init__(
        self,
        name: str = "app",
        level: LogLevel = LogLevel.INFO,
        show_time: bool = True,
    ):
        self.name = name
        self.level = level
        self.show_time = show_time
        self.console = Console() if HAS_RICH else None
    
    def _log(self, level: LogLevel, message: str, **kwargs) -> None:
        """Internal log method."""
        if level < self.level:
            return
        
        style = STYLES.get(level, STYLES[LogLevel.INFO])
        timestamp = datetime.now().strftime("%H:%M:%S") if self.show_time else ""
        
        if HAS_RICH and self.console:
            parts = []
            if timestamp:
                parts.append(f"[dim]{timestamp}[/]")
            parts.append(style.icon)
            parts.append(f"[{style.color}]{message}[/]")
            self.console.print(" ".join(parts))
        else:
            parts = []
            if timestamp:
                parts.append(timestamp)
            parts.append(style.icon)
            parts.append(message)
            print(" ".join(parts))
    
    def trace(self, msg: str, **kwargs) -> None:
        """Log trace message."""
        self._log(LogLevel.TRACE, msg, **kwargs)
    
    def debug(self, msg: str, **kwargs) -> None:
        """Log debug message."""
        self._log(LogLevel.DEBUG, msg, **kwargs)
    
    def info(self, msg: str, **kwargs) -> None:
        """Log info message."""
        self._log(LogLevel.INFO, msg, **kwargs)
    
    def success(self, msg: str, **kwargs) -> None:
        """Log success message."""
        self._log(LogLevel.SUCCESS, msg, **kwargs)
    
    def warning(self, msg: str, **kwargs) -> None:
        """Log warning message."""
        self._log(LogLevel.WARNING, msg, **kwargs)
    
    def warn(self, msg: str, **kwargs) -> None:
        """Alias for warning."""
        self.warning(msg, **kwargs)
    
    def error(self, msg: str, **kwargs) -> None:
        """Log error message."""
        self._log(LogLevel.ERROR, msg, **kwargs)
    
    def critical(self, msg: str, **kwargs) -> None:
        """Log critical message."""
        self._log(LogLevel.CRITICAL, msg, **kwargs)
    
    @contextmanager
    def timer(self, task: str):
        """Time a task."""
        self.info(f"Starting: {task}")
        start = time.time()
        try:
            yield
            elapsed = time.time() - start
            self.success(f"Completed: {task} ({elapsed:.2f}s)")
        except Exception as e:
            elapsed = time.time() - start
            self.error(f"Failed: {task} ({elapsed:.2f}s) - {e}")
            raise


# Global logger
_logger = Logger()


def configure(
    level: LogLevel = LogLevel.INFO,
    show_time: bool = True,
) -> None:
    """Configure global logger."""
    global _logger
    _logger.level = level
    _logger.show_time = show_time


def trace(msg: str, **kwargs) -> None:
    _logger.trace(msg, **kwargs)

def debug(msg: str, **kwargs) -> None:
    _logger.debug(msg, **kwargs)

def info(msg: str, **kwargs) -> None:
    _logger.info(msg, **kwargs)

def success(msg: str, **kwargs) -> None:
    _logger.success(msg, **kwargs)

def warning(msg: str, **kwargs) -> None:
    _logger.warning(msg, **kwargs)

def error(msg: str, **kwargs) -> None:
    _logger.error(msg, **kwargs)

def critical(msg: str, **kwargs) -> None:
    _logger.critical(msg, **kwargs)

def timer(task: str):
    return _logger.timer(task)


if __name__ == "__main__":
    print("CLI Logger Demo")
    print("=" * 40)
    
    log = Logger(level=LogLevel.TRACE)
    
    log.trace("Trace message")
    log.debug("Debug message")
    log.info("Info message")
    log.success("Success message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")
    
    print()
    with log.timer("Heavy task"):
        time.sleep(0.5)
