"""
"Quickly generating poster variations" video from Unit 3
"""

import py5

from unit_3.utils import star

seed = 1


def grid(offset_x, columns, rows):
    w = (py5.width - 2 * offset_x) / columns

    offset_y = (py5.height - w * rows) / 2

    for j in range(rows):
        pos_y = (j * w) + (w / 2) + offset_y

        r = py5.random_int(0, 128)
        g = py5.random_int(128, 255)
        b = py5.random_int(0, 255)

        for i in range(columns):
            pos_x = (i * w) + (w / 2) + offset_x

            m = py5.random_int(1, 6)

            if m == 1:
                py5.fill(r, g, b, 128)

                ra = py5.random(w / 20, w / 2)
                rb = py5.random(1, w / 2)
                np = py5.random_int(4, 10)
                star(pos_x, pos_y, ra, rb, np, animated=False)
            elif 1 < m < 4:
                py5.fill(255, 64)
                dr = py5.random_int(0, 1) * w / 2

                py5.rect(pos_x - dr, pos_y - dr, w / 2, w / 2)
            elif 4 <= m < 6:
                py5.rect(pos_x - w / 2, pos_y - w / 2, w, w)
            else:
                py5.fill(r, g, b, 64)
                py5.circle(pos_x, pos_y, py5.random_int(1, 2) * w / 4)


def setup():
    py5.size(700, 980)


def draw():
    py5.random_seed(seed)

    py5.background(0, 0, 100)
    py5.stroke(255)

    for _ in range(3):
        grid(100, 6, 8)


def mouse_pressed():
    global seed

    seed += 1
    print(f"Seed: {seed}")


def key_pressed():
    if py5.key == "s":
        file_name = f"output-{seed}.png"
        py5.save_frame(file_name)
        print(f"Saved frame at: {file_name}")


py5.run_sketch()
