from uuid import uuid7

from unit_3.utils import BaseSketch


class Sketch(BaseSketch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.save_document = False

    def settings(self):
        self.size(700, 980)

    def key_pressed(self):
        if self.key == "p":
            self.save_document = True
            print("Saving PDF...")

    def draw(self):
        if self.save_document:
            timestamp = uuid7()
            # self.begin_record(self.SVG, "output.svg")
            self.begin_record(self.PDF, f"output-{timestamp}.pdf")

        self.background(0, 0, 100)
        self.circle(
            self.width / 2,
            self.height / 2,
            200,
        )

        if self.save_document:
            self.end_record()
            self.save_document = False


if __name__ == "__main__":
    sketch = Sketch()
    sketch.run_sketch()
