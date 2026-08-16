"""
"Recursive Grid" video from Unit 4
"""

import py5

from unit_3.utils import star

save_document = False
seed = 1


def grid(offset_x, offset_y, columns, rows, sketch_width):
    w = sketch_width / columns

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
                py5.stroke(0)

                ra = py5.random(w / 20, w / 2)
                rb = py5.random(1, w / 2)
                np = py5.random_int(4, 10)
                star(pos_x, pos_y, ra, rb, np, animated=False)
            elif 1 < m < 4:
                py5.fill(255, 64)
                py5.stroke(r, g, b)
                dr = py5.random_int(0, 1) * w / 2

                py5.rect(pos_x - dr, pos_y - dr, w / 2, w / 2)
            elif 4 <= m < 6:
                py5.stroke(r, g, b)
                py5.rect(pos_x - w / 2, pos_y - w / 2, w, w)
            else:
                py5.stroke(0)
                py5.fill(r, g, b, 64)
                py5.circle(pos_x, pos_y, py5.random_int(1, 2) * w / 4)

            if py5.random_int(1, 3) == 3 and w > 30:
                grid(pos_x - w / 2, pos_y - w / 2, 2, 2, w)


def setup():
    py5.size(700, 980)


def draw():
    global seed

    output_name = f"poster_{seed}.pdf"
    print(f"Saving PDF for seed '{seed}': {output_name}")
    py5.begin_record(py5.PDF, output_name)

    py5.random_seed(seed)

    py5.background(0, 0, 100)
    py5.stroke(255)

    for _ in range(3):
        grid(50, 40, 4, 6, 600)

    py5.end_record()

    if seed == 20:
        py5.exit_sketch()

    seed += 1


def mouse_pressed():
    global seed

    seed += 1
    print(f"Seed: {seed}")


def key_pressed():
    global save_document

    if py5.key == "s":
        file_name = f"output-{seed}.png"
        py5.save_frame(file_name)
        print(f"Saved frame at: {file_name}")

    elif py5.key == "p":
        save_document = True


py5.run_sketch()
