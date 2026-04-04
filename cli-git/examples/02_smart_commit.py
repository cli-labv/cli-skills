#!/usr/bin/env python3
"""
Example: Smart commit workflow

Shows the complete commit flow with analysis and confirmation.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from skills.cli_git import smart_commit, suggest_message, analyze

def main():
    print("Smart Commit Example")
    print("=" * 50)
    
    try:
        # First, let's see what message would be generated
        print("\n1. Checking suggested message...")
        msg = suggest_message()
        
        if not msg:
            print("   No changes to commit")
            return
        
        print(f"\n   Suggested message:\n   {msg.split(chr(10))[0]}")
        
        # Now do the smart commit (interactive)
        print("\n2. Running smart commit...")
        print("   (This will ask for confirmation)\n")
        
        success = smart_commit(auto_push=False)
        
        if success:
            print("\n✅ Commit successful!")
        else:
            print("\n❌ Commit cancelled or failed")
            
    except ValueError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
