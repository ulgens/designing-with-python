"""
"How to define and use new functions" video from Unit 2
"""

import py5


def eye(x, y, width):
    py5.no_stroke()

    py5.fill(255)
    py5.ellipse(x, y, width, width / 3)

    py5.fill(255, 0, 0)
    py5.ellipse(x, y, width / 3, width / 3)

    py5.fill(0)
    py5.ellipse(x, y, width / 10, width / 10)


def setup():
    py5.size(980, 980)
    py5.background(0, 0, 200)

    for y in range(100, 1000, 100):
        eye(x=py5.width / 2, y=y, width=150)


py5.run_sketch()
