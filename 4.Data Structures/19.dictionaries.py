point = {"x": 1, "y": 2}

# Equivalent to above
point = dict(x=1, y=2)

print(point["x"])

point["x"] = 10
print(point["x"])

point["z"] = 20
print(point)

# Check if key exists
if "a" in point:
    print(point["a"])

point.get("a", 0)  # Returns 0 if key doesn't exist

del point["x"]
print(point)

# looping through keys
for key in point:
    print(key, point[key])