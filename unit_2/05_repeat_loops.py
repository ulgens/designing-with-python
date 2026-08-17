"""
"Repeat loops" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def setup(self):
        self.background(240)

        self.no_loop()

    def draw(self):
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
            self.line(n * 10, 100, n * 5, 490)

        margin = 50
        for i in range(20):
            self.line(margin + i * 8, 150, margin + i * 16, 600)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
