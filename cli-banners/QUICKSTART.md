# ⚡ Quick Start - CLI Banners Skill

Generate professional ASCII banners in 60 seconds.

## 🚀 Basic Usage

### Python

```python
# 1. Add to path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "skills/cli-banners/python"))

# 2. Import
from cli_banners import generate_text, generate_shape

# 3. Generate!
print(generate_text("HELLO", style="block", color="cyan"))
print(generate_shape("check", style="detailed", color="green"))
```

### Bash

```bash
# 1. Load
source skills/cli-banners/bash/banner_generator.sh

# 2. Generate!
generate_colored_banner "HELLO" "cyan"
generate_check detailed
```

## 📝 Three Essential Functions

### 1️⃣ `generate_text()` - ASCII Text

```python
generate_text("MYAPP", style="block", color="cyan")
```

**Output:**
```
 ███╗   ███╗  ██╗   ██╗   █████╗   ██████╗   ██████╗  
 ████╗ ████║  ╚██╗ ██╔╝  ██╔══██╗  ██╔══██╗  ██╔══██╗ 
 ██╔████╔██║   ╚████╔╝   ███████║  ██████╔╝  ██████╔╝ 
 ██║╚██╔╝██║    ╚██╔╝    ██╔══██║  ██╔═══╝   ██╔═══╝  
 ██║ ╚═╝ ██║     ██║     ██║  ██║  ██║       ██║      
 ╚═╝     ╚═╝     ╚═╝     ╚═╝  ╚═╝  ╚═╝       ╚═╝      
```

**Styles:** `block`, `minimal`

### 2️⃣ `generate_shape()` - Symbols & Icons

```python
check = generate_shape("check", style="detailed", color="green")
arrow = generate_shape("arrow_right", style="block")
star = generate_shape("star", style="block", color="yellow")

print(f"{check} Success")
print(f"{arrow} Next step")
print(f"{star} Featured")
```

**Available Shapes:**
- `arrow_right`, `arrow_left`, `arrow_up`, `arrow_down`
- `check`, `cross`, `star`, `heart`
- `loading`

**Styles:** `minimal`, `block`, `shaded`, `detailed`

### 3️⃣ Bash Helper Functions

```bash
generate_arrow right        # ▶
generate_check detailed     # ✅
generate_cross detailed     # ❌
generate_star block         # ★
```

## 🎨 Colors Available

```python
# Standard: red, green, yellow, blue, magenta, cyan, white
# Bright: bright_red, bright_green, bright_yellow, etc.

generate_text("SUCCESS", color="bright_green")
generate_text("ERROR", color="bright_red")
generate_text("INFO", color="cyan")
```

## 💡 Common Use Cases

### Welcome Banner

```python
from cli_banners import generate_text

print(generate_text("MYAPP", style="block", color="cyan"))
print("  Version 1.0.0 - Production Ready\n")
```

### Status Messages

```python
from cli_banners import generate_shape

check = generate_shape("check", style="detailed", color="green")
cross = generate_shape("cross", style="detailed", color="red")

print(f"{check} Build successful")
print(f"{cross} Tests failed")
```

### Interactive Menu

```python
arrow = generate_shape("arrow_right", style="block")

print("Main Menu:")
print(f"  {arrow} Option 1")
print(f"  {arrow} Option 2")
print(f"  {arrow} Exit")
```

### Deployment Script

```bash
source skills/cli-banners/bash/banner_generator.sh

generate_colored_banner "DEPLOY" "cyan"
echo ""

arrow=$(generate_arrow right)
echo "$arrow Building..."
sleep 2

check=$(generate_check detailed)
echo "$check Build complete"
```

## 🔍 See the Demo

```bash
# Full demo
python3 skills/cli-banners/python/cli_banners.py

# Bash demo
bash skills/cli-banners/bash/banner_generator.sh
```

## 📚 More Info

- **Full docs:** `skills/cli-banners/README.md`
- **Examples:** `skills/cli-banners/examples/`

## ❓ Quick Tips

1. **No dependencies**: Works anywhere Python/Bash runs
2. **Combine with perfect-boxes**: Use both skills together
3. **Colors optional**: Leave out for plain ASCII
4. **Styles matter**: `block` for bold, `minimal` for clean

---

**Ready to use!** Start generating professional CLI banners now. 🎨
