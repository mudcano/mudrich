Render Groups
=============

The :class:`~rich.console.RenderGroup` class allows you to group several renderables together so they may be rendered in a context where only a single renderable may be supplied. For instance, you might want to display several renderables within a :class:`~rich.panel.Panel`.

To render two panels within a third panel, you would construct a RenderGroup with the *child* renderables as positional arguments then wrap the result in another Panel::

    from mudrich import print
    from mudrich.console import RenderGroup
    from mudrich.panel import Panel

    panel_group = RenderGroup(
        Panel("Hello", style="on blue"),
        Panel("World", style="on red"),
    )
    print(Panel(panel_group))


This pattern is nice when you know in advance what renderables will be in a group, but can get awkward if you have a larger number of renderables, especially if they are dynamic. Rich provides a :func:`~rich.console.render_group` decorator to help with these situations. The decorator builds a render group from an iterator of renderables. The following is the equivalent of the previous example using the decorator::

    from mudrich import print
    from mudrich.console import render_group
    from mudrich.panel import Panel

    @render_group()
    def get_panels():
        yield Panel("Hello", style="on blue")
        yield Panel("World", style="on red")

    print(Panel(get_panels()))
