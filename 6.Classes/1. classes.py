class Point:
    def draw(self):
        print("draw")

point = Point()
point.draw()  # This will output: draw
print(type(point))  # This will output: <class '__main__.Point'>
print(isinstance(point, Point))  # This will output: True