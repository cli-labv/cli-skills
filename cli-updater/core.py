"""
Core implementation of CLI Updater.

Version checking from PyPI and GitHub.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.request import urlopen
from urllib.error import URLError

try:
    from rich.console import Console
    from rich.panel import Panel
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


@dataclass
class UpdateInfo:
    """Update information."""
    current: str
    latest: str
    has_update: bool
    install_cmd: str = ""


class VersionChecker:
    """
    Version checker for CLI applications.
    
    Example:
        >>> checker = VersionChecker("myapp", "1.0.0")
        >>> update = checker.check_pypi()
        >>> if update.has_update:
        ...     checker.print_notice(update)
    """
    
    CACHE_DIR = Path.home() / ".cache" / "cli-updater"
    CACHE_TTL = 86400  # 24 hours
    
    def __init__(
        self,
        name: str,
        current_version: str,
        use_cache: bool = True,
    ):
        self.name = name
        self.current = current_version
        self.use_cache = use_cache
        self.CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    def _cache_path(self) -> Path:
        return self.CACHE_DIR / f"{self.name}.json"
    
    def _read_cache(self) -> Optional[str]:
        """Read cached version."""
        if not self.use_cache:
            return None
        try:
            path = self._cache_path()
            if not path.exists():
                return None
            data = json.loads(path.read_text())
            if time.time() - data["time"] > self.CACHE_TTL:
                return None
            return data["version"]
        except:
            return None
    
    def _write_cache(self, version: str) -> None:
        """Write version to cache."""
        if not self.use_cache:
            return
        try:
            self._cache_path().write_text(json.dumps({
                "version": version,
                "time": time.time()
            }))
        except:
            pass
    
    def _compare_versions(self, v1: str, v2: str) -> int:
        """Compare versions. Returns 1 if v2 > v1, -1 if v1 > v2, 0 if equal."""
        def parse(v):
            return [int(x) for x in v.lstrip("v").split(".")]
        try:
            p1, p2 = parse(v1), parse(v2)
            for a, b in zip(p1, p2):
                if b > a: return 1
                if a > b: return -1
            return len(p2) - len(p1)
        except:
            return 0
    
    def check_pypi(self) -> UpdateInfo:
        """Check PyPI for updates."""
        # Try cache first
        cached = self._read_cache()
        if cached:
            return UpdateInfo(
                current=self.current,
                latest=cached,
                has_update=self._compare_versions(self.current, cached) > 0,
                install_cmd=f"pip install --upgrade {self.name}"
            )
        
        try:
            url = f"https://pypi.org/pypi/{self.name}/json"
            with urlopen(url, timeout=3) as r:
                data = json.loads(r.read())
                latest = data["info"]["version"]
                self._write_cache(latest)
                return UpdateInfo(
                    current=self.current,
                    latest=latest,
                    has_update=self._compare_versions(self.current, latest) > 0,
                    install_cmd=f"pip install --upgrade {self.name}"
                )
        except:
            return UpdateInfo(self.current, self.current, False)
    
    def check_github(self, owner: str, repo: str) -> UpdateInfo:
        """Check GitHub releases for updates."""
        cached = self._read_cache()
        if cached:
            return UpdateInfo(
                current=self.current,
                latest=cached,
                has_update=self._compare_versions(self.current, cached) > 0,
                install_cmd=f"https://github.com/{owner}/{repo}/releases"
            )
        
        try:
            url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
            with urlopen(url, timeout=3) as r:
                data = json.loads(r.read())
                latest = data["tag_name"].lstrip("v")
                self._write_cache(latest)
                return UpdateInfo(
                    current=self.current,
                    latest=latest,
                    has_update=self._compare_versions(self.current, latest) > 0,
                    install_cmd=f"https://github.com/{owner}/{repo}/releases"
                )
        except:
            return UpdateInfo(self.current, self.current, False)
    
    def print_notice(self, update: UpdateInfo) -> None:
        """Print update notice."""
        if not update.has_update:
            return
        
        msg = f"Update available: {update.current} → {update.latest}"
        cmd = f"Run: {update.install_cmd}"
        
        if HAS_RICH:
            console.print(Panel(
                f"[yellow]{msg}[/]\n[dim]{cmd}[/]",
                title="🔄 Update Available",
                border_style="yellow"
            ))
        else:
            print(f"\n🔄 {msg}")
            print(f"   {cmd}\n")


def check_update(
    name: str,
    current: str,
    source: str = "pypi",
    owner: str = "",
    repo: str = "",
) -> UpdateInfo:
    """Check for updates."""
    checker = VersionChecker(name, current)
    if source == "github" and owner and repo:
        return checker.check_github(owner, repo)
    return checker.check_pypi()


def print_update_notice(
    name: str,
    current: str,
    source: str = "pypi",
    owner: str = "",
    repo: str = "",
) -> None:
    """Check and print update notice if available."""
    checker = VersionChecker(name, current)
    if source == "github" and owner and repo:
        update = checker.check_github(owner, repo)
    else:
        update = checker.check_pypi()
    checker.print_notice(update)


if __name__ == "__main__":
    print("CLI Updater Demo")
    
    # Example: Check requests package
    checker = VersionChecker("requests", "2.0.0")  # Old version
    update = checker.check_pypi()
    
    print(f"Current: {update.current}")
    print(f"Latest: {update.latest}")
    print(f"Has update: {update.has_update}")
    
    if update.has_update:
        checker.print_notice(update)
