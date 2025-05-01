items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

#def sort_item(item):
#    return item[1]

items.sort(key=lambda item:item[1])
print(items)