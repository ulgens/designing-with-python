"""
"How to define and use new functions" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def eye(self, x, y, width):
        self.no_stroke()

        self.fill(255)
        self.ellipse(x, y, width, width / 3)

        self.fill(255, 0, 0)
        self.ellipse(x, y, width / 3, width / 3)

        self.fill(0)
        self.ellipse(x, y, width / 10, width / 10)

    def setup(self):
        self.background(0, 0, 200)

        for y in range(100, 1000, 100):
            self.eye(x=self.width / 2, y=y, width=150)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
