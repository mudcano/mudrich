"""
This example demonstrates the justify argument to print.
"""

from mudrich.console import Console
from mudrich.panel import Panel

console = Console(width=20)

style = "bold white on blue"
panel = Panel("Rich", style="on red", expand=False)
console.print(panel, style=style)
console.print(panel, style=style, justify="left")
console.print(panel, style=style, justify="center")
console.print(panel, style=style, justify="right")
