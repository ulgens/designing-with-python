"""
"Repeat loops" video from Unit 2
"""

import py5


def setup():
    py5.size(980, 980)
    py5.background(240)

    # List example
    fruits = [
        "kiwi",
        "acai",
        "banana",
    ]
    for f in fruits:
        print(f)

    # Tuple example
    p = (200, 100)  # noqa: F841

    # Drawing lines with a loop
    step_size = 2
    for n in range(10, 70, step_size):
        py5.line(n * 10, 100, n * 5, 490)

    margin = 50
    for i in range(20):
        py5.line(margin + i * 8, 150, margin + i * 16, 600)


py5.run_sketch()
