
def add(number1, number2):
    num1 = number1          # KISS being ignored. There's no need to assign to new variable.
    num2 = number2
    total = 0
    total = total + num1
    total = total + num2    # specific example of DRY being ignored
    return total

def subtract(number1, number2):
    pass
def multiply(number1, number2):
    pass
def divide(number1, number2):
    pass

number1 = 3     # example of YAGNI being ignored.
number2 = 6     # making more variable than needed, or not putting into a list
number3 = 8     # or not asking the user for numbers
number4 = 2
number5 = 5
number6 = 9

print(add(number6, number5))