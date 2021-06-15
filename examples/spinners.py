from time import sleep

from mudrich.columns import Columns
from mudrich.panel import Panel
from mudrich.live import Live
from mudrich.text import Text
from mudrich.spinner import Spinner, SPINNERS

all_spinners = Columns(
    [
        Spinner(spinner_name, text=Text(repr(spinner_name), style="green"))
        for spinner_name in sorted(SPINNERS)
    ],
    column_first=True,
    expand=True,
)

with Live(
    Panel(all_spinners, title="Spinners", border_style="blue"),
    refresh_per_second=20,
) as live:
    while True:
        sleep(0.1)
