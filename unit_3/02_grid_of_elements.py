"""
"A grid of ordered elements" video from Unit 3
"""

from unit_3.utils import BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(700, 980)

    def setup(self):
        self.background(0, 0, 100)

        columns, rows = 10, 15

        offset_x = 50
        w = (self.width - 2 * offset_x) / columns
        print(f"Width: {w}")

        offset_y = (self.height - w * rows) / 2

        for j in range(rows):
            pos_y = (j * w) + (w / 2) + offset_y

            for i in range(columns):
                pos_x = (i * w) + (w / 2) + offset_x

                self.star(
                    pos_x,
                    pos_y,
                    w / (2 + j),
                    w / 4,
                    np=3 + i,
                )


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
