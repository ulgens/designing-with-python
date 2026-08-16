from py5 import Sketch

__all__ = ("BaseSketch",)


class BaseSketch(Sketch):
    def star(self, cx, cy, ra, rb, np, start_angle=0, animated=True):
        step = self.TWO_PI / np

        self.begin_shape()

        for i in range(np):
            angle = start_angle + step * i
            if animated:
                angle += self.frame_count / 50.0

            ax = cx + self.cos(angle) * ra
            ay = cy + self.sin(angle) * ra
            self.vertex(ax, ay)
            bx = cx + self.cos(angle + step / 2.0) * rb
            by = cy + self.sin(angle + step / 2.0) * rb
            self.vertex(bx, by)

        self.end_shape(self.CLOSE)
