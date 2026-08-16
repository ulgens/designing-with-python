from uuid import uuid7

import py5

save_document = False


def setup():
    py5.size(700, 980)


def draw():
    global save_document
    if save_document:
        timestamp = uuid7()
        # py5.begin_record(py5.SVG, "output.svg")
        py5.begin_record(py5.PDF, f"output-{timestamp}.pdf")

    py5.background(0, 0, 100)
    py5.circle(
        py5.width / 2,
        py5.height / 2,
        200,
    )

    if save_document:
        py5.end_record()
        save_document = False


def key_pressed():
    global save_document

    if py5.key == "p":
        save_document = True
        print("Saving PDF...")


py5.run_sketch()
