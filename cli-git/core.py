"""
CLI Git - Smart Git Workflow Automation

Features:
1. Analyze changes and detect file movements vs deletions
2. Alert on dangerous changes (important file deletions)
3. Auto-generate descriptive commit messages
4. Guided commit flow (analyze → confirm → commit → push)

Design: Clean code, single responsibility per function
"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from difflib import SequenceMatcher

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class FileChange:
    """Represents a single file change."""
    path: str
    status: str  # added, modified, deleted, renamed, moved
    old_path: Optional[str] = None
    is_dangerous: bool = False
    danger_reason: str = ""


@dataclass
class ChangeAnalysis:
    """Complete analysis of git changes."""
    added: List[FileChange] = field(default_factory=list)
    modified: List[FileChange] = field(default_factory=list)
    deleted: List[FileChange] = field(default_factory=list)
    moved: List[FileChange] = field(default_factory=list)
    renamed: List[FileChange] = field(default_factory=list)
    
    has_dangerous: bool = False
    dangerous_changes: List[FileChange] = field(default_factory=list)
    
    @property
    def total_changes(self) -> int:
        return (len(self.added) + len(self.modified) + 
                len(self.deleted) + len(self.moved) + len(self.renamed))
    
    @property
    def is_empty(self) -> bool:
        return self.total_changes == 0


# =============================================================================
# CONFIGURATION
# =============================================================================

DANGEROUS_PATTERNS = [
    "*.py", "*.js", "*.ts", "*.go", "*.rs", "*.java",
    "requirements.txt", "pyproject.toml", "setup.py",
    "package.json", "Cargo.toml", "go.mod",
    ".env", "docker-compose.yml", "Dockerfile",
    "README.md", "LICENSE",
]

SAFE_TO_DELETE = [
    "*.pyc", "__pycache__/*", "*.log", "*.tmp",
    ".DS_Store", "Thumbs.db", "*.egg-info/*",
    "dist/*", "build/*",
]


# =============================================================================
# GIT COMMANDS
# =============================================================================

def run_git(args: List[str], cwd: str = None) -> Tuple[bool, str]:
    """Run a git command and return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            cwd=cwd or os.getcwd(),
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def is_git_repo(path: str = None) -> bool:
    """Check if directory is a git repository."""
    success, _ = run_git(["rev-parse", "--git-dir"], path)
    return success


def get_status_porcelain() -> List[str]:
    """Get git status in porcelain format."""
    success, output = run_git(["status", "--porcelain", "-uall"])
    if not success:
        return []
    return [line for line in output.strip().split("\n") if line]


# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def parse_status_line(line: str) -> Tuple[str, str, Optional[str]]:
    """Parse a git status porcelain line."""
    if not line or len(line) < 3:
        return "", "", None
    
    status = line[:2].strip()
    rest = line[3:]
    
    if " -> " in rest:
        old_path, new_path = rest.split(" -> ")
        return status, new_path, old_path
    
    return status, rest, None


def similarity_ratio(s1: str, s2: str) -> float:
    """Calculate similarity between two strings."""
    return SequenceMatcher(None, s1, s2).ratio()


def detect_file_moves(deleted: List[str], added: List[str]) -> List[Tuple[str, str]]:
    """Detect files that were moved (deleted + added with same name)."""
    moves = []
    used_added = set()
    
    for del_path in deleted:
        del_name = Path(del_path).name
        
        for add_path in added:
            if add_path in used_added:
                continue
            
            add_name = Path(add_path).name
            
            if del_name == add_name:
                moves.append((del_path, add_path))
                used_added.add(add_path)
                break
            elif similarity_ratio(del_name, add_name) > 0.8:
                moves.append((del_path, add_path))
                used_added.add(add_path)
                break
    
    return moves


def is_pattern_match(filepath: str, pattern: str) -> bool:
    """Check if filepath matches a glob-like pattern."""
    if pattern.startswith("*"):
        return filepath.endswith(pattern[1:])
    if pattern.endswith("*"):
        return filepath.startswith(pattern[:-1])
    if "*" in pattern:
        parts = pattern.split("*")
        return filepath.startswith(parts[0]) and filepath.endswith(parts[-1])
    return filepath == pattern or filepath.endswith("/" + pattern)


def is_dangerous_delete(filepath: str) -> Tuple[bool, str]:
    """Check if deleting this file is dangerous."""
    for pattern in SAFE_TO_DELETE:
        if is_pattern_match(filepath, pattern):
            return False, ""
    
    for pattern in DANGEROUS_PATTERNS:
        if is_pattern_match(filepath, pattern):
            return True, f"Archivo importante: {pattern}"
    
    return False, ""


class GitAnalyzer:
    """
    Analyzes git repository changes.
    
    Example:
        >>> analyzer = GitAnalyzer()
        >>> analysis = analyzer.analyze()
        >>> analyzer.print_summary(analysis)
    """
    
    def __init__(self, path: str = None):
        self.path = path or os.getcwd()
        
        if not is_git_repo(self.path):
            raise ValueError(f"No es un repositorio git: {self.path}")
    
    def analyze(self) -> ChangeAnalysis:
        """Analyze all changes in the repository."""
        analysis = ChangeAnalysis()
        status_lines = get_status_porcelain()
        
        raw_added = []
        raw_deleted = []
        
        for line in status_lines:
            status, filepath, old_path = parse_status_line(line)
            
            if not status:
                continue
            
            if status.startswith("R"):
                analysis.renamed.append(FileChange(filepath, "renamed", old_path))
                continue
            
            if "M" in status:
                analysis.modified.append(FileChange(filepath, "modified"))
                continue
            
            if status in ("A", "??", "A "):
                raw_added.append(filepath)
                continue
            
            if "D" in status:
                raw_deleted.append(filepath)
                continue
        
        # Detect moves
        moves = detect_file_moves(raw_deleted, raw_added)
        moved_old = set()
        moved_new = set()
        
        for old_path, new_path in moves:
            analysis.moved.append(FileChange(new_path, "moved", old_path))
            moved_old.add(old_path)
            moved_new.add(new_path)
        
        # Process remaining
        for filepath in raw_added:
            if filepath not in moved_new:
                analysis.added.append(FileChange(filepath, "added"))
        
        for filepath in raw_deleted:
            if filepath not in moved_old:
                is_danger, reason = is_dangerous_delete(filepath)
                change = FileChange(filepath, "deleted", is_dangerous=is_danger, danger_reason=reason)
                analysis.deleted.append(change)
                
                if is_danger:
                    analysis.has_dangerous = True
                    analysis.dangerous_changes.append(change)
        
        return analysis
    
    def print_summary(self, analysis: ChangeAnalysis = None) -> None:
        """Print a summary of changes."""
        if analysis is None:
            analysis = self.analyze()
        
        if analysis.is_empty:
            _print_msg("✅ No hay cambios pendientes")
            return
        
        if HAS_RICH:
            self._print_rich(analysis)
        else:
            self._print_plain(analysis)
    
    def _print_rich(self, analysis: ChangeAnalysis) -> None:
        """Print with rich formatting."""
        content = []
        
        if analysis.moved:
            content.append("[bold cyan]📁 MOVIMIENTOS DETECTADOS[/]")
            for c in analysis.moved:
                content.append(f"   {c.old_path} → [green]{c.path}[/]")
            content.append("")
        
        if analysis.renamed:
            content.append("[bold blue]✏️  RENOMBRADOS[/]")
            for c in analysis.renamed:
                content.append(f"   {c.old_path} → [blue]{c.path}[/]")
            content.append("")
        
        if analysis.added:
            content.append("[bold green]➕ NUEVOS[/]")
            for c in analysis.added:
                content.append(f"   [green]{c.path}[/]")
            content.append("")
        
        if analysis.modified:
            content.append("[bold yellow]📝 MODIFICADOS[/]")
            for c in analysis.modified:
                content.append(f"   [yellow]{c.path}[/]")
            content.append("")
        
        if analysis.deleted:
            content.append("[bold red]🗑️  ELIMINADOS[/]")
            for c in analysis.deleted:
                if c.is_dangerous:
                    content.append(f"   [bold red]⚠️  {c.path}[/] (¡PELIGROSO!)")
                else:
                    content.append(f"   [red]{c.path}[/]")
            content.append("")
        
        if analysis.has_dangerous:
            content.append("[bold white on red] ⚠️  ATENCIÓN: Hay eliminaciones de archivos importantes [/]")
        
        console.print(Panel("\n".join(content), title="📊 Análisis de Cambios", border_style="cyan"))
    
    def _print_plain(self, analysis: ChangeAnalysis) -> None:
        """Print without formatting."""
        print("\n" + "=" * 50)
        print("  📊 Análisis de Cambios")
        print("=" * 50)
        
        if analysis.moved:
            print("\n📁 MOVIMIENTOS DETECTADOS:")
            for c in analysis.moved:
                print(f"   {c.old_path} → {c.path}")
        
        if analysis.renamed:
            print("\n✏️  RENOMBRADOS:")
            for c in analysis.renamed:
                print(f"   {c.old_path} → {c.path}")
        
        if analysis.added:
            print("\n➕ NUEVOS:")
            for c in analysis.added:
                print(f"   {c.path}")
        
        if analysis.modified:
            print("\n📝 MODIFICADOS:")
            for c in analysis.modified:
                print(f"   {c.path}")
        
        if analysis.deleted:
            print("\n🗑️  ELIMINADOS:")
            for c in analysis.deleted:
                prefix = "⚠️ " if c.is_dangerous else ""
                print(f"   {prefix}{c.path}")
        
        if analysis.has_dangerous:
            print("\n" + "!" * 50)
            print("  ⚠️  ATENCIÓN: Eliminaciones peligrosas detectadas")
            print("!" * 50)


# =============================================================================
# COMMIT MESSAGE GENERATION
# =============================================================================

def determine_change_type(analysis: ChangeAnalysis) -> str:
    """Determine the main type of change for commit prefix."""
    if analysis.moved:
        destinations = [Path(c.path).parts[0] for c in analysis.moved]
        if all(d == "docs" for d in destinations):
            return "docs"
        if all(d == "tests" for d in destinations):
            return "test"
        if all(d == "scripts" for d in destinations):
            return "chore"
        return "refactor"
    
    if analysis.added and not analysis.modified and not analysis.deleted:
        first = analysis.added[0].path
        if first.startswith("tests/") or "test" in first:
            return "test"
        if first.startswith("docs/") or first.endswith(".md"):
            return "docs"
        return "feat"
    
    all_paths = [c.path for c in analysis.added + analysis.modified + analysis.moved]
    if all_paths and all(p.startswith("docs/") or p.endswith(".md") for p in all_paths):
        return "docs"
    
    if analysis.modified:
        return "fix"
    
    return "chore"


def generate_commit_message(analysis: ChangeAnalysis) -> str:
    """Generate a descriptive commit message."""
    if analysis.is_empty:
        return ""
    
    prefix = determine_change_type(analysis)
    lines = []
    
    # Title
    if analysis.moved:
        destinations = set(Path(c.path).parts[0] for c in analysis.moved)
        if len(destinations) == 1:
            lines.append(f"{prefix}: mover archivos a {list(destinations)[0]}/")
        else:
            lines.append(f"{prefix}: reorganizar estructura del proyecto")
    elif analysis.added and not analysis.modified:
        if len(analysis.added) == 1:
            lines.append(f"{prefix}: agregar {analysis.added[0].path}")
        else:
            lines.append(f"{prefix}: agregar {len(analysis.added)} archivos")
    elif analysis.modified and len(analysis.modified) == 1:
        lines.append(f"{prefix}: actualizar {analysis.modified[0].path}")
    else:
        lines.append(f"{prefix}: actualizar proyecto")
    
    # Body
    lines.append("")
    
    if analysis.moved:
        for c in analysis.moved[:5]:
            lines.append(f"- Mover {Path(c.old_path).name} → {Path(c.path).parent}/")
        if len(analysis.moved) > 5:
            lines.append(f"- ... y {len(analysis.moved) - 5} más")
    
    if analysis.added:
        for c in analysis.added[:5]:
            lines.append(f"- Agregar {c.path}")
        if len(analysis.added) > 5:
            lines.append(f"- ... y {len(analysis.added) - 5} más")
    
    if analysis.modified:
        for c in analysis.modified[:5]:
            lines.append(f"- Actualizar {c.path}")
    
    if analysis.deleted:
        for c in analysis.deleted[:3]:
            lines.append(f"- Eliminar {c.path}")
    
    return "\n".join(lines)


# =============================================================================
# HIGH-LEVEL FUNCTIONS
# =============================================================================

def analyze(path: str = None, print_summary: bool = True) -> ChangeAnalysis:
    """
    Analyze changes in a git repository.
    
    Example:
        >>> analysis = analyze()
        >>> if analysis.has_dangerous:
        ...     print("¡Cambios peligrosos!")
    """
    analyzer = GitAnalyzer(path)
    analysis = analyzer.analyze()
    
    if print_summary:
        analyzer.print_summary(analysis)
    
    return analysis


def suggest_message(path: str = None) -> str:
    """
    Suggest a commit message based on changes.
    
    Example:
        >>> msg = suggest_message()
        >>> print(msg)
    """
    analyzer = GitAnalyzer(path)
    analysis = analyzer.analyze()
    return generate_commit_message(analysis)


def smart_commit(
    path: str = None,
    auto_push: bool = False,
    custom_message: str = None,
) -> bool:
    """
    Smart commit flow: analyze → confirm → add → commit → push.
    
    Example:
        >>> smart_commit(auto_push=True)
    """
    try:
        analyzer = GitAnalyzer(path)
        analysis = analyzer.analyze()
        
        if analysis.is_empty:
            _print_msg("✅ No hay cambios para commit")
            return True
        
        analyzer.print_summary(analysis)
        
        message = custom_message or generate_commit_message(analysis)
        
        _print_msg("\n💡 Mensaje de commit sugerido:")
        _print_msg("-" * 40)
        _print_msg(message)
        _print_msg("-" * 40)
        
        if analysis.has_dangerous:
            _print_msg("\n⚠️  ADVERTENCIA: Eliminaciones peligrosas detectadas:")
            for c in analysis.dangerous_changes:
                _print_msg(f"   - {c.path}")
        
        # Confirm
        if HAS_RICH:
            proceed = Confirm.ask("\n¿Proceder con el commit?", default=True)
        else:
            response = input("\n¿Proceder? [S/n]: ").strip().lower()
            proceed = response in ("", "s", "si", "sí", "y", "yes")
        
        if not proceed:
            _print_msg("❌ Commit cancelado")
            return False
        
        # Git operations
        success, output = run_git(["add", "."], path)
        if not success:
            _print_msg(f"❌ Error en git add: {output}")
            return False
        
        success, output = run_git(["commit", "-m", message], path)
        if not success:
            _print_msg(f"❌ Error en git commit: {output}")
            return False
        
        _print_msg("✅ Commit realizado")
        
        if auto_push:
            _print_msg("📤 Pushing...")
            success, output = run_git(["push"], path)
            if not success:
                _print_msg(f"⚠️  Error en push: {output}")
                return False
            _print_msg("✅ Push completado")
        
        return True
        
    except Exception as e:
        _print_msg(f"❌ Error: {e}")
        return False


def quick_push(message: str = None, path: str = None) -> bool:
    """
    Quick add + commit + push with auto-generated message.
    
    Example:
        >>> quick_push()  # Auto message
        >>> quick_push("fix: corregir bug")  # Custom
    """
    return smart_commit(path=path, auto_push=True, custom_message=message)


def _print_msg(msg: str) -> None:
    """Print message."""
    if HAS_RICH:
        console.print(msg)
    else:
        print(msg)


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    import sys
    
    args = sys.argv[1:] if len(sys.argv) > 1 else ["help"]
    cmd = args[0]
    
    if cmd == "analyze":
        analyze()
    elif cmd == "suggest":
        print("\n" + suggest_message())
    elif cmd == "commit":
        smart_commit()
    elif cmd == "push":
        quick_push()
    else:
        print("Uso: python -m cli_git [analyze|suggest|commit|push]")
        print("\n  analyze  - Analizar cambios")
        print("  suggest  - Sugerir mensaje de commit")
        print("  commit   - Commit interactivo")
        print("  push     - Commit + push rápido")
