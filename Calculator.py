import sys

def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Dividing by zero."
        result /= num
    return result

def calculator():
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <number1> <number2> [more numbers...] <operation>")
        return

    try:
        *numbers_str, operation = sys.argv[1:]
        numbers = [float(n) for n in numbers_str]
    except ValueError:
        print("Error: Not valid numbers.")
        return

    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        print("Error: Unsupported operation. Choose from: +,-,*,/.")
        return

    result = operations[operation](*numbers)
    print("Result:", result)

if __name__ == "__main__":
    calculator()
