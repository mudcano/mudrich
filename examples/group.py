from mudrich import print
from mudrich.console import RenderGroup
from mudrich.panel import Panel

panel_group = RenderGroup(
    Panel("Hello", style="on blue"),
    Panel("World", style="on red"),
)
print(Panel(panel_group))
