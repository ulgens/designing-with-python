"""
"Randomness: Infinite options 2" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def star(self, cx, cy, ra, rb, np, start_angle=0):
        step = self.TWO_PI / np

        self.fill(119)

        self.begin_shape()
        for i in range(np):
            ang = start_angle + step * i + self.frame_count / 50.0
            ax = cx + self.cos(ang) * ra
            ay = cy + self.sin(ang) * ra
            self.vertex(ax, ay)
            bx = cx + self.cos(ang + step / 2.0) * rb
            by = cy + self.sin(ang + step / 2.0) * rb
            self.vertex(bx, by)
        self.end_shape(self.CLOSE)

    def setup(self):
        self.fill(0)
        self.no_stroke()

        self.rect_mode(self.CENTER)

        for x in range(50, 930, 100):
            n = self.random_int(3, 7)
            r = self.random_choice((10, 25, 40))

            self.star(x, 100, r, 50, n)

        for x in range(50, 930, 100):
            v = self.random_int(1, 5)

            if v == 1:
                self.circle(x, 450, 50)
            elif v == 2:
                self.square(x, 450, 50)
            else:
                r = self.random_choice((10, 25, 40))
                self.star(x, 450, r, 30, v)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
