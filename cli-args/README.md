# CLI Args ⚙️

Simplified argument parsing for Python CLI applications.

## Installation

```bash
pip install typer
```

## Quick Start

```python
from skills.cli_args import App, Argument, Option

app = App("myapp", "My CLI tool", version="1.0.0")

@app.command()
def greet(
    name: str = Argument(..., help="Name"),
    loud: bool = Option(False, help="Shout", short="l"),
):
    msg = f"Hello, {name}!"
    print(msg.upper() if loud else msg)

app.run()
```

## Features

### App

```python
app = App("myapp", "Description", version="1.0.0")

@app.command()
def cmd1(): pass

@app.command(name="other", help="Other command")
def cmd2(): pass

app.run()
```

### Arguments and Options

```python
# Required argument
name: str = Argument(..., help="Name")

# Optional argument with default
name: str = Argument("World", help="Name")

# Boolean flag
verbose: bool = Option(False, help="Verbose", short="v")

# String option
output: str = Option("out.txt", help="Output file")
```

### Single Function CLI

```python
from skills.cli_args import run, Argument, Option

def main(
    name: str = Argument(...),
    count: int = Option(1),
):
    for _ in range(count):
        print(f"Hello {name}")

run(main)
```

## License

MIT
