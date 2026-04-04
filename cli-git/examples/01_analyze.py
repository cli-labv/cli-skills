#!/usr/bin/env python3
"""
Example: Analyze git changes

Shows how to analyze repository changes and detect moves.
"""

import os
import sys

# Add parent to path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from skills.cli_git import analyze

def main():
    print("Git Change Analysis Example")
    print("=" * 50)
    
    try:
        # Analyze current directory
        analysis = analyze()
        
        # Access results programmatically
        print("\n📊 Summary:")
        print(f"  Moved:    {len(analysis.moved)}")
        print(f"  Renamed:  {len(analysis.renamed)}")
        print(f"  Added:    {len(analysis.added)}")
        print(f"  Modified: {len(analysis.modified)}")
        print(f"  Deleted:  {len(analysis.deleted)}")
        
        if analysis.has_dangerous:
            print("\n⚠️  Dangerous changes detected!")
            for change in analysis.dangerous_changes:
                print(f"  - {change.path}: {change.danger_reason}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("   Make sure you're in a git repository")


if __name__ == "__main__":
    main()
