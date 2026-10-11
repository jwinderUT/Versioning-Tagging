import math
def calculate(operation, a, b):
    if operation in ['subtract', 'minus', '-']:
        x = (a - b)
        print(x)
    elif operation in ['multiply', 'times', '*']:
        x = (a * b)
        print(x)
    elif operation in ['divide', 'by', '/']:
        if b == 0:
            print("Exception: Cannot divide by 0.")
        else:
            x = (a / b)
            print(x)
    elif operation in ['average', 'mean']:
        x = (a + b) / 2
        print(x)
    elif operation in ["log", 'logarithm', 'logarighm']:
        x = math.log(a, b)
        print(x)
    else:
        print("Error: Unsupported operation")

# Example usage
if __name__ == "__main__":
    calculate('add', 5, 3)        # Output: 8
    calculate('subtract', 5, 3)   # Output: 2
    calculate('multiply', 5, 3)   # Output: 15
    calculate('divide', 5, 3)     # Output: 1.666...
    calculate('divide', 5, 0)     # Error