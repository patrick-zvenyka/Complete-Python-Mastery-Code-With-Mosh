class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point at ({self.x}, {self.y})")

point = Point(10, 20)
point.draw()  # This will output: draw
print(point.x)  # This will output: 10