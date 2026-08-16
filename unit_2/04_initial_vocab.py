"""
"Initial py5 drawing vocabulary" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def setup(self):
        self.background(200, 0, 200)
        self.rect_mode(self.CENTER)

    def draw(self):
        # Rectangle
        self.fill(0, 200, 0)
        self.stroke(255, 0, 0)
        self.stroke_weight(5)

        self.rect(self.width / 2, self.height / 2, 200, 50)

        # Ellipse
        self.fill(255)
        self.no_stroke()

        self.ellipse(200, 200, 100, 100)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
