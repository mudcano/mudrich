from typing import Any


def load_ipython_extension(ip: Any) -> None:  # pragma: no cover
    # prevent circular import
    from mudrich.pretty import install
    from mudrich.traceback import install as tr_install

    install()
    tr_install()
