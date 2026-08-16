"""
"Quickly generating poster variations" video from Unit 3
"""

from unit_3.utils import BaseSketch


class Sketch(BaseSketch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.seed = 1

    def settings(self):
        self.size(700, 980)

    def setup(self):
        print(f"Seed: {self.seed}")

    def key_pressed(self):
        if self.key == "s":
            file_name = f"output-{self.seed}.png"
            self.save_frame(file_name)
            print(f"Saved frame at: {file_name}")

    def mouse_pressed(self):
        self.seed += 1
        print(f"Seed: {self.seed}")

    def grid(self, offset_x, columns, rows):
        w = (self.width - 2 * offset_x) / columns

        offset_y = (self.height - w * rows) / 2

        for j in range(rows):
            pos_y = (j * w) + (w / 2) + offset_y

            r = self.random_int(0, 128)
            g = self.random_int(128, 255)
            b = self.random_int(0, 255)

            for i in range(columns):
                pos_x = (i * w) + (w / 2) + offset_x

                m = self.random_int(1, 6)

                if m == 1:
                    self.fill(r, g, b, 128)

                    ra = self.random(w / 20, w / 2)
                    rb = self.random(1, w / 2)
                    np = self.random_int(4, 10)
                    self.star(pos_x, pos_y, ra, rb, np, animated=False)
                elif 1 < m < 4:
                    self.fill(255, 64)
                    dr = self.random_int(0, 1) * w / 2

                    self.rect(pos_x - dr, pos_y - dr, w / 2, w / 2)
                elif 4 <= m < 6:
                    self.rect(pos_x - w / 2, pos_y - w / 2, w, w)
                else:
                    self.fill(r, g, b, 64)
                    self.circle(pos_x, pos_y, self.random_int(1, 2) * w / 4)

    def draw(self):
        self.random_seed(self.seed)

        self.background(0, 0, 100)
        self.stroke(255)

        for _ in range(3):
            self.grid(100, 6, 8)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
