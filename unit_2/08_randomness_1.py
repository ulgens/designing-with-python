"""
"Randomness: Infinite options 1" video from Unit 2
"""

import py5


def setup():
    py5.size(980, 980)

    n = py5.random(10)
    print(n)

    i = py5.random_int(0, 10)
    print(i)

    py5.fill(0)
    py5.no_stroke()

    for x in range(50, 930, 50):
        d = py5.random(50)

        py5.circle(x, 50, d)

    for x in range(50, 930, 50):
        i = py5.random_int(1, 4)

        py5.circle(x, 150, i * 10)

    for x in range(50, 930, 50):
        r = py5.random_int(255)
        g = py5.random_int(255)
        b = py5.random_int(255)

        py5.fill(r, g, b)

        py5.circle(x, 250, 45)

    for x in range(50, 930, 50):
        r = 0
        g = py5.random_int(255)
        b = py5.random_int(255)

        py5.fill(r, g, b)

        py5.circle(x, 350, 45)

    for x in range(50, 930, 50):
        r = 0
        g = py5.random_int(128, 255)
        b = 128

        py5.fill(r, g, b)

        py5.circle(x, 450, 45)

    cores = [
        py5.color(255, 200, 0),
        py5.color(0, 128, 255),
        py5.color(128, 255, 0),
    ]

    for x in range(50, 930, 50):
        py5.fill(py5.random_choice(cores))

        py5.circle(x, 550, 45)


py5.run_sketch()
