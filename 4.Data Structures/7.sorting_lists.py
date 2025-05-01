numbers = [3,51,2,8,6]
# ascending order
numbers.sort()
sorted(numbers)
print(numbers)

# descending order
numbers.sort(reverse=True)
sorted(numbers, reverse=True)
print(numbers)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)