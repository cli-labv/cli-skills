"""
Core implementation of CLI Wizard.

Multi-step configuration wizards using questionary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

try:
    import questionary
    from questionary import Style
    HAS_QUESTIONARY = True
except ImportError:
    HAS_QUESTIONARY = False

try:
    from rich.console import Console
    from rich.panel import Panel
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


@dataclass
class Step:
    """A wizard step."""
    key: str
    prompt: str
    type: str = "text"  # text, password, select, checkbox, confirm
    default: Any = None
    choices: List[Any] = field(default_factory=list)
    validate: Optional[Callable[[Any], bool]] = None
    condition: Optional[Callable[[Dict], bool]] = None


@dataclass
class WizardResult:
    """Result of wizard execution."""
    data: Dict[str, Any]
    completed: bool = True
    
    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)
    
    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        return dict(self.data)


class Wizard:
    """
    Multi-step configuration wizard.
    
    Example:
        >>> wizard = Wizard("Project Setup")
        >>> wizard.add_text("name", "Project name")
        >>> wizard.add_select("type", "Project type", ["web", "cli", "api"])
        >>> wizard.add_confirm("typescript", "Use TypeScript?")
        >>> 
        >>> result = wizard.run()
        >>> print(result["name"])
    """
    
    def __init__(
        self,
        title: str = "Setup Wizard",
        description: str = "",
    ):
        if not HAS_QUESTIONARY:
            raise ImportError("questionary required: pip install questionary")
        
        self.title = title
        self.description = description
        self.steps: List[Step] = []
    
    def add_text(
        self,
        key: str,
        prompt: str,
        default: str = "",
        validate: Optional[Callable] = None,
    ) -> "Wizard":
        """Add text input step."""
        self.steps.append(Step(key, prompt, "text", default, validate=validate))
        return self
    
    def add_password(self, key: str, prompt: str) -> "Wizard":
        """Add password input step."""
        self.steps.append(Step(key, prompt, "password"))
        return self
    
    def add_select(
        self,
        key: str,
        prompt: str,
        choices: List[Any],
        default: Any = None,
    ) -> "Wizard":
        """Add single selection step."""
        self.steps.append(Step(key, prompt, "select", default, choices))
        return self
    
    def add_checkbox(
        self,
        key: str,
        prompt: str,
        choices: List[Any],
        default: List[Any] = None,
    ) -> "Wizard":
        """Add multiple selection step."""
        self.steps.append(Step(key, prompt, "checkbox", default or [], choices))
        return self
    
    def add_confirm(
        self,
        key: str,
        prompt: str,
        default: bool = False,
    ) -> "Wizard":
        """Add yes/no step."""
        self.steps.append(Step(key, prompt, "confirm", default))
        return self
    
    def add_conditional(
        self,
        key: str,
        prompt: str,
        condition: Callable[[Dict], bool],
        type: str = "text",
        **kwargs,
    ) -> "Wizard":
        """Add conditional step."""
        step = Step(key, prompt, type, condition=condition, **kwargs)
        self.steps.append(step)
        return self
    
    def run(self) -> WizardResult:
        """Run the wizard."""
        # Print header
        if HAS_RICH:
            console.print(Panel(
                f"[bold]{self.title}[/bold]\n{self.description}",
                border_style="cyan"
            ))
        else:
            print(f"\n{'='*50}")
            print(f"  {self.title}")
            print(f"{'='*50}\n")
        
        data: Dict[str, Any] = {}
        
        for i, step in enumerate(self.steps, 1):
            # Check condition
            if step.condition and not step.condition(data):
                continue
            
            # Show progress
            print(f"\n  Step {i}/{len(self.steps)}")
            
            # Get input based on type
            try:
                if step.type == "text":
                    value = questionary.text(
                        step.prompt,
                        default=step.default or "",
                        validate=step.validate,
                    ).ask()
                elif step.type == "password":
                    value = questionary.password(step.prompt).ask()
                elif step.type == "select":
                    value = questionary.select(
                        step.prompt,
                        choices=step.choices,
                        default=step.default,
                    ).ask()
                elif step.type == "checkbox":
                    value = questionary.checkbox(
                        step.prompt,
                        choices=step.choices,
                    ).ask()
                elif step.type == "confirm":
                    value = questionary.confirm(
                        step.prompt,
                        default=step.default,
                    ).ask()
                else:
                    value = questionary.text(step.prompt).ask()
                
                if value is None:
                    return WizardResult({}, completed=False)
                
                data[step.key] = value
                
            except KeyboardInterrupt:
                return WizardResult(data, completed=False)
        
        print("\n  ✅ Wizard completed!\n")
        return WizardResult(data, completed=True)


if __name__ == "__main__":
    print("CLI Wizard Demo")
    
    wizard = Wizard("Project Setup", "Configure your new project")
    wizard.add_text("name", "Project name:", default="my-project")
    wizard.add_select("type", "Project type:", ["web", "cli", "api", "library"])
    wizard.add_confirm("typescript", "Use TypeScript?", default=True)
    wizard.add_checkbox("features", "Select features:", [
        "auth", "database", "testing", "docker"
    ])
    
    result = wizard.run()
    
    if result.completed:
        print(f"Project: {result['name']}")
        print(f"Type: {result['type']}")
        print(f"TypeScript: {result['typescript']}")
        print(f"Features: {result['features']}")
