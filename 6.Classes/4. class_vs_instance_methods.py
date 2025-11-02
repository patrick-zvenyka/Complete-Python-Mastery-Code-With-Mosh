class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(1, 2) 

    def draw(self):
        print(f"Point at ({self.x}, {self.y})")

point = Point.zero 
point.draw()  # This will output: Point at (1, 2)
