class Point:
    default_color = "red"  # Class attribute
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point at ({self.x}, {self.y})")

point_1 = Point(10, 20)
point_2 = Point(30, 40)
Point.default_color = "blue"  # Modifying class attribute
print(Point.default_color)  # Accessing class attribute via class
print(point_1.default_color)  # Accessing class attribute via instance
point_1.z = 30  # Adding a new instance attribute 'z'
point_1.draw()  # This will output: draw
