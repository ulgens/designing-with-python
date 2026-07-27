import py5

__all__ = ("star",)


def star(cx, cy, ra, rb, np, start_angle=0, animated=True):
    step = py5.TWO_PI / np

    py5.begin_shape()
    for i in range(np):
        angle = start_angle + step * i
        if animated:
            angle += py5.frame_count / 50.0

        ax = cx + py5.cos(angle) * ra
        ay = cy + py5.sin(angle) * ra
        py5.vertex(ax, ay)
        bx = cx + py5.cos(angle + step / 2.0) * rb
        by = cy + py5.sin(angle + step / 2.0) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)
