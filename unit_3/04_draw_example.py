import py5

seed = 1


def setup():
    py5.size(980, 980)


def draw():
    # Clean
    py5.background(200)

    # Setup?
    py5.random_seed(seed)

    # Draw
    d = py5.random_int(100, 200)

    r = py5.random_int(255)
    g = py5.random_int(255)
    b = py5.random_int(255)
    py5.fill(r, g, b)

    py5.circle(
        py5.width / 2,
        py5.height / 2,
        d,
    )


def mouse_pressed():
    global seed  # I don't like this
    seed += 1
    print(seed)

    py5.redraw()


py5.run_sketch()
