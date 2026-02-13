# A simple Calculator program - Good Version following KISS, DRY, and YAGNI principles

# functions for each operation, keeping them simple and no extra features.
def add(a,b):
    return a+b # directly returns the result without additional variables

def subtract(a,b):
    return a-b # simple and clear code with no extra steps

def multiply(a,b): # KISS: doesn't use loops
    return a*b # DRY: no repeated addition logic, directly multiplying

def divide(a,b):
    if b == 0: # DRY: No repeated subtraction logic
        return "Error: Cannot divide by zero"
    else:
        return a/b #YAGNI: Only handles the division needed for this program

# main function to handle user input
def main():
    print("Welcome to Good Calculator!")
    # KISS: Directly ask user for input.
    # YAGNI: No hardcoded variables
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    # DRY: Used a  dictionary dispatch instead of multiple if/elif statements.
    # KISS: Clear mapping between operator and function.
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    # KISS: Single conditional check.
    # DRY: Avoid repeated conditional blocks.
    if operation in operations:
        print(operations[operation](num1, num2))
    else:
        print("Invalid operation")

main()
