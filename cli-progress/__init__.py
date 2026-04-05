"""CLI Progress - Modern progress indicators powered by alive-progress."""
from .core import (
    spinner,
    progress,
    manual_progress,
    track,
    track_download,
    countdown,
    TaskGroup,
    show_all_spinners,
    show_all_bars,
    show_all_themes,
    SPINNERS,
)

__version__ = "3.0.0"
__all__ = [
    "spinner",
    "progress",
    "manual_progress",
    "track",
    "track_download",
    "countdown",
    "TaskGroup",
    "show_all_spinners",
    "show_all_bars",
    "show_all_themes",
    "SPINNERS",
]
