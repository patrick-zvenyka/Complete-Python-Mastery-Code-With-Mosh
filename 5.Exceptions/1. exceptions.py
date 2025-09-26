numbers = [1,2]
#print(numbers[3])  # This will raise an IndexError
try:
    print(numbers[3])
except IndexError as e:
    print("An error occurred:", e)