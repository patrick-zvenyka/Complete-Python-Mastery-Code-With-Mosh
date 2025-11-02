from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or negative.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor is None:
    pass
"""


timeit_result1 = timeit(code2, number=10000)
print(f"Time with exception handling: {timeit_result1}")