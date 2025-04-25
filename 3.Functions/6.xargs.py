
def multiply(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print(multiply(2,3,4,5))