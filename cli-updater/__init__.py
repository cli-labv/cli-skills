"""CLI Updater - Version checking and updates."""
from .core import VersionChecker, check_update, print_update_notice
__version__ = "2.0.0"
__all__ = ["VersionChecker", "check_update", "print_update_notice"]
