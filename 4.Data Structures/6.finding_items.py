letters = ["a","b","c","d"]
item = str(input("Enter item: "))
if item in letters:
    print(letters.index(item))
else:
    print(f"Item {item} not in the list")