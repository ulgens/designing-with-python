"""
"Randomness: Infinite options 1" video from Unit 2
"""

from py5 import Sketch as BaseSketch


class Sketch(BaseSketch):
    def settings(self):
        self.size(980, 980)

    def setup(self):
        n = self.random(10)
        print(n)

        i = self.random_int(0, 10)
        print(i)

        self.fill(0)
        self.no_stroke()

        for x in range(50, 930, 50):
            d = self.random(50)

            self.circle(x, 50, d)

        for x in range(50, 930, 50):
            i = self.random_int(1, 4)

            self.circle(x, 150, i * 10)

        for x in range(50, 930, 50):
            r = self.random_int(255)
            g = self.random_int(255)
            b = self.random_int(255)

            self.fill(r, g, b)

            self.circle(x, 250, 45)

        for x in range(50, 930, 50):
            r = 0
            g = self.random_int(255)
            b = self.random_int(255)

            self.fill(r, g, b)

            self.circle(x, 350, 45)

        for x in range(50, 930, 50):
            r = 0
            g = self.random_int(128, 255)
            b = 128

            self.fill(r, g, b)

            self.circle(x, 450, 45)

        cores = [
            self.color(255, 200, 0),
            self.color(0, 128, 255),
            self.color(128, 255, 0),
        ]

        for x in range(50, 930, 50):
            self.fill(self.random_choice(cores))

            self.circle(x, 550, 45)


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
