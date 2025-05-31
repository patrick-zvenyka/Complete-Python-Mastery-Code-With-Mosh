items = [
    ("Product1", 10),
    ('Product2', 9),
    ("Product3", 12),
]

# filtering products costing at least 10 and above
x=list(filter(lambda item: item[1] >= 10, items))
print(x)

