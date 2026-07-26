"""
"Randomness: Infinite options 2" video from Unit 2
"""

import py5


def star(cx, cy, ra, rb, np, start_angle=0):
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

    py5.fill(0)
    py5.no_stroke()

    py5.rect_mode(py5.CENTER)

    for x in range(50, 930, 100):
        n = py5.random_int(3, 7)
        r = py5.random_choice((10, 25, 40))

        star(x, 100, r, 50, n)

    for x in range(50, 930, 100):
        v = py5.random_int(1, 5)

        if v == 1:
            py5.circle(x, 450, 50)
        elif v == 2:
            py5.square(x, 450, 50)
        else:
            r = py5.random_choice((10, 25, 40))
            star(x, 450, r, 30, v)


py5.run_sketch()
