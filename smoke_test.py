"""
A simple sketch to smoke test the local env setup.
Successful run should render a rectangle window with mouse drawing smaller rectangles.
"""

import py5


def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


py5.run_sketch()
