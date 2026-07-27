"""
"A grid of ordered elements" video from Unit 3
"""

import py5

from unit_3.utils import star


def setup():
    py5.size(700, 980)
    py5.background(0, 0, 100)

    columns, rows = 10, 15

    offset_x = 50
    w = (py5.width - 2 * offset_x) / columns
    print(f"Width: {w}")

    offset_y = (py5.height - w * rows) / 2

    for j in range(rows):
        pos_y = (j * w) + (w / 2) + offset_y

        for i in range(columns):
            pos_x = (i * w) + (w / 2) + offset_x

            star(
                pos_x,
                pos_y,
                w / (2 + j),
                w / 4,
                np=3 + i,
            )


py5.run_sketch()
