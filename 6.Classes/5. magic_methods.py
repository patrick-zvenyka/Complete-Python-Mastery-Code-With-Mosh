class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def draw(self):
        print(f"Point at ({self.x}, {self.y})")

point = Point(10, 20)

print(point)  # This will output something like: <__main__.Point object at 0x...>