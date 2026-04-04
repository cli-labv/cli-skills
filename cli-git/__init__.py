"""CLI Git - Smart Git workflow automation."""
from .core import (
    GitAnalyzer,
    analyze,
    suggest_message,
    smart_commit,
    quick_push,
)

__version__ = "1.0.0"
__all__ = [
    "GitAnalyzer",
    "analyze",
    "suggest_message",
    "smart_commit",
    "quick_push",
]
