import io

from mudrich.abc import RichRenderable
from mudrich.console import Console
from mudrich.panel import Panel
from mudrich.text import Text


class Foo:
    def __rich__(self) -> Text:
        return Text("Foo")


def test_rich_cast():
    foo = Foo()
    console = Console(file=io.StringIO())
    console.print(foo)
    assert console.file.getvalue() == "Foo\n"


def test_rich_cast_container():
    foo = Foo()
    console = Console(file=io.StringIO(), legacy_windows=False)
    console.print(Panel.fit(foo, padding=0))
    assert console.file.getvalue() == "╭───╮\n│Foo│\n╰───╯\n"


def test_abc():
    foo = Foo()
    assert isinstance(foo, RichRenderable)
    assert isinstance(Text("hello"), RichRenderable)
    assert isinstance(Panel("hello"), RichRenderable)
    assert not isinstance(foo, str)
    assert not isinstance("foo", RichRenderable)
    assert not isinstance([], RichRenderable)
