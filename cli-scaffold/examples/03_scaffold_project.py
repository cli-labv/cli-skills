#!/usr/bin/env python3
"""
Example: Scaffold a complete project

Shows how to create a full project structure.
"""

import tempfile
import os
from pathlib import Path

from skills.cli_scaffold import scaffold_project

def main():
    print("Project Scaffolding Example")
    print("=" * 50)
    
    # Create in temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"\nCreating project in: {tmpdir}")
        
        # Scaffold python-cli project
        created = scaffold_project(
            name="awesome-cli",
            path=tmpdir,
            template="python-cli"
        )
        
        print("\nCreated files:")
        print("-" * 50)
        
        for path, type_ in sorted(created.items()):
            rel_path = path.replace(tmpdir + "/", "")
            icon = "📁" if type_ == "folder" else "📄"
            print(f"  {icon} {rel_path}")
        
        # Show tree structure
        print("\n\nProject Tree:")
        print("-" * 50)
        
        project_path = Path(tmpdir) / "awesome-cli"
        
        for root, dirs, files in os.walk(project_path):
            level = root.replace(str(project_path), "").count(os.sep)
            indent = "  " * level
            folder_name = os.path.basename(root)
            print(f"{indent}📁 {folder_name}/")
            
            subindent = "  " * (level + 1)
            for file in sorted(files):
                print(f"{subindent}📄 {file}")
        
        # Show start.sh content
        start_sh = project_path / "start.sh"
        print("\n\nstart.sh help output:")
        print("-" * 50)
        
        os.system(f"bash {start_sh} help 2>/dev/null || echo 'Preview only'")


if __name__ == "__main__":
    main()
