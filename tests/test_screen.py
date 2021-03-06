from mudrich.console import Console
from mudrich.screen import Screen


def test_screen():
    console = Console(color_system=None, width=20, height=5)
    with console.capture() as capture:
        console.print(Screen("foo\nbar\nbaz\nfoo\nbar\nbaz\foo"))
    result = capture.get()
    print(repr(result))
    expected = "foo                 \nbar                 \nbaz                 \nfoo                 \nbar                 "
    assert result == expected
