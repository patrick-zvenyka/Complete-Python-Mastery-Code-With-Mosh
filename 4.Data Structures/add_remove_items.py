letters = ["a","b","c"]

# Add
letters.append("d")
letters.insert(0,"-")
print(letters)

# Remove
letters.pop()
print(letters)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)