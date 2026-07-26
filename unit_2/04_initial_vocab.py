"""
"Initial py5 drawing vocabulary" video from Unit 2
"""

import py5

# TODO:
#   Wildcard import from py5 causes multiple issues like
#   > RuntimeError: Cannot call the size() method here. Either move it to a settings() function or move it to closer to the start of setup().
#   > NameError: name 'width' is not defined
#   I'm not sure what is going on.


def setup():
    py5.size(980, 980)

    py5.background(200, 0, 200)

    py5.rect_mode(py5.CENTER)


def draw():
    # Rectangle
    py5.fill(0, 200, 0)
    py5.stroke(255, 0, 0)
    py5.stroke_weight(5)

    py5.rect(py5.width / 2, py5.height / 2, 200, 50)

    # Ellipse
    py5.fill(255)
    py5.no_stroke()

    py5.ellipse(200, 200, 100, 100)


py5.run_sketch()
