numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: 1 2 3 4 5

# Using unpacking operator
print(*numbers)  # Output: 1 2 3 4 5

# Merging lists using unpacking operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

# Using unpacking operator with range
values=[*range(5)]
print(values)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]