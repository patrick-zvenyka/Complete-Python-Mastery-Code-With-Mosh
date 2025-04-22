command = ""
while True:
    command = input(">").lower()
    print("ECHO", command)

    if command == "quit":
        break
