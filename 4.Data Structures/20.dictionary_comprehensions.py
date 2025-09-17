# Traditional way of creating a list
values  = []
for i in range(5):
    values.append(i*2)

#[expression for item in iterable if condition]
values = [i*2 for i in range(5)]
print(values)

# Dictionary comprehension
squares = {i: i*i for i in range(5)}  
print(squares)