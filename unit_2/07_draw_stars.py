"""
"Function to draw stars" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def star4(self, xc, yc, wa, wb):
        pts = (
            (-wa, -wa),
            (0, -wb),
            (wa, -wa),
            (wb, 0),
            (wa, wa),
            (0, wb),
            (-wa, wa),
            (-wb, 0),
        )

        self.begin_shape()
        for x, y in pts:
            self.vertex(x + xc, y + yc)
        self.end_shape(self.CLOSE)

    def star5(self, cx, cy, ra, rb, np, start_angle=0):
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
        self.background(0, 0, 200)

        self.no_loop()

    def draw(self):
        # Example polygon
        pts = (
            (200, 200),
            (500, 100),
            (400, 400),
            (300, 200),
            (100, 500),
        )

        self.begin_shape()
        for x, y in pts:
            self.vertex(x, y)
        self.end_shape(self.CLOSE)

        # Stars
        self.star4(700, 300, 200, 100)
        self.star4(500, 400, 150, 50)

        self.star5(300, 300, 200, 100, 7)
        self.star5(600, 600, 150, 50, 11)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
