from mudrich.control import Control, strip_control_codes
from mudrich.segment import Segment, ControlType


def test_control():
    control = Control(ControlType.BELL)
    assert str(control) == "\x07"


def test_strip_control_codes():
    assert strip_control_codes("") == ""
    assert strip_control_codes("foo\rbar") == "foobar"
    assert strip_control_codes("Fear is the mind killer") == "Fear is the mind killer"


def test_control_move_to():
    control = Control.move_to(5, 10)
    print(control.segment)
    assert control.segment == Segment(
        "\x1b[11;6H", None, [(ControlType.CURSOR_MOVE_TO, 5, 10)]
    )


def test_control_move():
    assert Control.move(0, 0).segment == Segment("", None, [])
    control = Control.move(3, 4)
    print(repr(control.segment))
    assert control.segment == Segment(
        "\x1b[3C\x1b[4B",
        None,
        [(ControlType.CURSOR_FORWARD, 3), (ControlType.CURSOR_DOWN, 4)],
    )


def test_move_to_row():
    print(repr(Control.move_to_row(10, 20).segment))
    assert Control.move_to_row(10, 20).segment == Segment(
        "\x1b[12G\x1b[20B",
        None,
        [(ControlType.CURSOR_MOVE_TO_ROW, 11), (ControlType.CURSOR_DOWN, 20)],
    )
