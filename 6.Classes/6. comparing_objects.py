class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __gt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) > (other.x, other.y)
        return NotImplemented
    
# Example usage:
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)
print(p1 == p2)  # True
print(p1 > p3)  # False