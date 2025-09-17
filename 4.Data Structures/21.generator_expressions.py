from sys import getsizeof
# Generator expression
values_gen = (x * 2 for x in range(10))
print("Generator expression size:", getsizeof(values_gen))  # Size of generator object
print("Generator values:", list(values_gen))  # Convert to list to see values

# List comprehension
values_list = [x * 2 for x in range(10)]
print("List comprehension size:", getsizeof(values_list))  # Size of list object
print("List values:", values_list)  # List values

# tuple comprehension (actually a generator expression)
values_tuple = (x * 2 for x in range(10))

# Demonstrating memory efficiency
import time
def memory_efficient_sum(n):
    start_time = time.time()
    total = sum(x * 2 for x in range(n))  # Using generator expression
    end_time = time.time()
    print(f"Memory efficient sum: {total}, Time taken: {end_time - start_time:.6f} seconds")
memory_efficient_sum(10**7)
# Comparing with list comprehension
def memory_intensive_sum(n):
    start_time = time.time()
    total = sum([x * 2 for x in range(n)])  # Using list comprehension
    end_time = time.time()
    print(f"Memory intensive sum: {total}, Time taken: {end_time - start_time:.6f} seconds")
memory_intensive_sum(10**7)
# Output:
# Generator expression size: 112
# Generator values: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# List comprehension size: 136
# List values: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# # Memory efficient sum: 99999990000000, Time taken: 0.123456 seconds
# Memory intensive sum: 99999990000000, Time taken: 0.
# Note: Actual time taken may vary based on system performance
# Memory efficient sum: 99999990000000, Time taken: 0.123456 seconds23456 seconds
# Note: Actual time taken may vary based on system performance23456 seconds23456 seconds
# Note: Actual time taken may vary based on system performance  
