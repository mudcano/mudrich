import sys

from mudrich.segment import ControlType
from mudrich.segment import Segment, Segments
from mudrich.style import Style


def test_repr():
    assert repr(Segment("foo")) == "Segment('foo', None)"
    home = (ControlType.HOME, 0)
    if sys.version_info >= (3, 10):
        assert (
            repr(Segment("foo", None, [home]))
            == "Segment('foo', None, [(ControlType.HOME, 0)])"
        )
    else:
        assert (
            repr(Segment("foo", None, [home]))
            == "Segment('foo', None, [(<ControlType.HOME: 3>, 0)])"
        )


def test_line():
    assert Segment.line() == Segment("\n")


def test_apply_style():
    segments = [Segment("foo"), Segment("bar", Style(bold=True))]
    assert Segment.apply_style(segments, None) is segments
    assert list(Segment.apply_style(segments, Style(italic=True))) == [
        Segment("foo", Style(italic=True)),
        Segment("bar", Style(italic=True, bold=True)),
    ]


def test_split_lines():
    lines = [Segment("Hello\nWorld")]
    assert list(Segment.split_lines(lines)) == [[Segment("Hello")], [Segment("World")]]


def test_split_and_crop_lines():
    assert list(
        Segment.split_and_crop_lines([Segment("Hello\nWorld!\n"), Segment("foo")], 4)
    ) == [
        [Segment("Hell"), Segment("\n", None)],
        [Segment("Worl"), Segment("\n", None)],
        [Segment("foo"), Segment(" ")],
    ]


def test_adjust_line_length():
    line = [Segment("Hello", "foo")]
    assert Segment.adjust_line_length(line, 10, style="bar") == [
        Segment("Hello", "foo"),
        Segment("     ", "bar"),
    ]

    line = [Segment("H"), Segment("ello, World!")]
    assert Segment.adjust_line_length(line, 5) == [Segment("H"), Segment("ello")]

    line = [Segment("Hello")]
    assert Segment.adjust_line_length(line, 5) == line


def test_get_line_length():
    assert Segment.get_line_length([Segment("foo"), Segment("bar")]) == 6


def test_get_shape():
    assert Segment.get_shape([[Segment("Hello")]]) == (5, 1)
    assert Segment.get_shape([[Segment("Hello")], [Segment("World!")]]) == (6, 2)


def test_set_shape():
    assert Segment.set_shape([[Segment("Hello")]], 10) == [
        [Segment("Hello"), Segment("     ")]
    ]
    assert Segment.set_shape([[Segment("Hello")]], 10, 2) == [
        [Segment("Hello"), Segment("     ")],
        [Segment(" " * 10)],
    ]


def test_simplify():
    assert list(
        Segment.simplify([Segment("Hello"), Segment(" "), Segment("World!")])
    ) == [Segment("Hello World!")]
    assert list(
        Segment.simplify(
            [Segment("Hello", "red"), Segment(" ", "red"), Segment("World!", "blue")]
        )
    ) == [Segment("Hello ", "red"), Segment("World!", "blue")]
    assert list(Segment.simplify([])) == []


def test_filter_control():
    control_code = (ControlType.HOME, 0)
    segments = [Segment("foo"), Segment("bar", None, (control_code,))]
    assert list(Segment.filter_control(segments)) == [Segment("foo")]
    assert list(Segment.filter_control(segments, is_control=True)) == [
        Segment("bar", None, (control_code,))
    ]


def test_strip_styles():
    segments = [Segment("foo", Style(bold=True))]
    assert list(Segment.strip_styles(segments)) == [Segment("foo", None)]


def test_strip_links():
    segments = [Segment("foo", Style(bold=True, link="https://www.example.org"))]
    assert list(Segment.strip_links(segments)) == [Segment("foo", Style(bold=True))]


def test_remove_color():
    segments = [
        Segment("foo", Style(bold=True, color="red")),
        Segment("bar", None),
    ]
    assert list(Segment.remove_color(segments)) == [
        Segment("foo", Style(bold=True)),
        Segment("bar", None),
    ]


def test_is_control():
    assert Segment("foo", Style(bold=True)).is_control == False
    assert Segment("foo", Style(bold=True), []).is_control == True
    assert Segment("foo", Style(bold=True), [(ControlType.HOME, 0)]).is_control == True


def test_segments_renderable():
    segments = Segments([Segment("foo")])
    assert list(segments.__rich_console__(None, None)) == [Segment("foo")]

    segments = Segments([Segment("foo")], new_lines=True)
    assert list(segments.__rich_console__(None, None)) == [
        Segment("foo"),
        Segment.line(),
    ]
