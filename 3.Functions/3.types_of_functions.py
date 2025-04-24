# Two types of functions
# 1 - perform a task - it prints result on the terminal only
def greet(name):
    print(f"Hi, {name}")


# 2 - return a value - returns a value, which can be used on terminal or writing into a file
def get_greeting(name):
    return f"Hie {name}"

message = get_greeting("Patrick")
# printing on terminal
print(message)

# writing a file
file = open("content.txt","w")
file.write(message)
