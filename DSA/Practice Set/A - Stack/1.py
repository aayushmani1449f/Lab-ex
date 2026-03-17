stack = []

def visit(stack, url):
    stack.append(url)

def back(stack):
    if len(stack) <= 1:
        print("No previous page")
    else:
        stack.pop()

def current(stack):
    if len(stack) > 0:
        print(stack[-1])

while True:
    command = input().split()

    if command[0] == "visit":
        visit(stack, command[1])

    elif command[0] == "back":
        back(stack)

    elif command[0] == "current":
        current(stack)
        break