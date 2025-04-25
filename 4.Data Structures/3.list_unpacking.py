numbers = [1,2,3]
numbers_2 = [1,2,3,4,5,6,7,8,9]
#unpacking lists

first, second, third = numbers
print(first)

first_1, second_1, *other, last = numbers_2
print(other)