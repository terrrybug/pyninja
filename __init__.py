"""
🥷 PyNinja - The Ultimate Python Dependency Ninja

Strike down outdated dependencies with stealth and precision!
"""

__version__ = "1.0.0"
__author__ = "PyNinja Community"
__email__ = "community@pyninja.dev"
__license__ = "MIT"
__description__ = "🥷 The Ultimate Python Dependency Ninja - automate, secure, and modernize your requirements"

# Import main classes for easy access
try:
    from .core.ninja import PyNinja
    from .core.analyzer import DependencyAnalyzer
    from .core.parser import RequirementsParser
    from .cli import main
    __all__ = [
        "PyNinja",
        "DependencyAnalyzer",
        "RequirementsParser",
        "main",
        "__version__"
    ]
except ImportError:
    __all__ = ["__version__"]

def _show_ninja_banner():
    """Show ninja banner on first import"""
    try:
        from rich.console import Console
        console = Console()
        console.print("🥷 [bold blue]PyNinja loaded - Ready to strike![/bold blue]")
    except ImportError:
