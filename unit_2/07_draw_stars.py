"""
"Function to draw stars" video from Unit 2
"""

import py5


def star4(xc, yc, wa, wb):
    pts = (
        (-wa, -wa),
        (0, -wb),
        (wa, -wa),
        (wb, 0),
        (wa, wa),
        (0, wb),
        (-wa, wa),
        (-wb, 0),
    )

    py5.begin_shape()
    for x, y in pts:
        py5.vertex(x + xc, y + yc)
    py5.end_shape(py5.CLOSE)


def star5(cx, cy, ra, rb, np, start_angle=0):
    step = py5.TWO_PI / np

    py5.fill(119)

    py5.begin_shape()
    for i in range(np):
        ang = start_angle + step * i + py5.frame_count / 50.0
        ax = cx + py5.cos(ang) * ra
        ay = cy + py5.sin(ang) * ra
        py5.vertex(ax, ay)
        bx = cx + py5.cos(ang + step / 2.0) * rb
        by = cy + py5.sin(ang + step / 2.0) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)


def setup():
    py5.size(980, 980)
    py5.background(0, 0, 200)

    # Example polygon
    pts = (
        (200, 200),
        (500, 100),
        (400, 400),
        (300, 200),
        (100, 500),
    )

    py5.begin_shape()
    for x, y in pts:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

    # Stars
    star4(700, 300, 200, 100)
    star4(500, 400, 150, 50)

    star5(300, 300, 200, 100, 7)
    star5(600, 600, 150, 50, 11)


py5.run_sketch()
