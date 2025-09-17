# Demonstrating basic set operations in Python
# Creating a set from a list

numbers = [1, 2, 3, 4, 5]

unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Adding an element
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Checking membership
print(4 in unique_numbers)  # Output: True

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))        # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b)) # Output: {3}
print(set_a.difference(set_b))   # Output: {1, 2}
print(set_a.symmetric_difference(set_b))  # Output: {1, 2, 4, 5}

# Frozenset (immutable set)
immutable_set = frozenset([1, 2, 3])
print(immutable_set)  # Output: frozenset({1, 2, 3})

# Set comprehension
squared_set = {x**2 for x in range(5)}  
print(squared_set)  # Output: {0, 1, 4, 9, 16}


first =set[1, 2, 3]
second =set[3, 4, 5]
print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)  # symmetric difference
print(first <= second) # subset
print(first >= second) # superset
print(first.isdisjoint(second)) # disjoint
print(len(first))      # length
first.add(6)          # add element
first.remove(2)       # remove element
first.clear()         # clear all elements
print(first)          # print set
print(second)         # print set
print(frozenset([1, 2, 3])) # frozenset
print({x**2 for x in range(5)}) # set comprehension
print({x for x in range(10) if x % 2 == 0}) # set comprehension with condition
print({x: x**2 for x in range(5)}) # dictionary comprehension