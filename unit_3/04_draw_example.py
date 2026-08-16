from unit_3.utils import BaseSketch


class Sketch(BaseSketch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.seed = 1

    def settings(self):
        self.size(980, 980)

    def setup(self):
        print(self.seed)

    def mouse_pressed(self):
        self.seed += 1
        print(self.seed)

        self.redraw()

    def draw(self):

        # Clean
        self.background(200)

        # Setup?
        self.random_seed(self.seed)

        # Draw
        d = self.random_int(100, 200)

        r = self.random_int(255)
        g = self.random_int(255)
        b = self.random_int(255)
        self.fill(r, g, b)

        self.circle(
            self.width / 2,
            self.height / 2,
            d,
        )


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
