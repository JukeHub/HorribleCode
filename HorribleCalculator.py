
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

# absolutely unnecessary method. User can just enter ints or we can typecast strings on request.
# This makes YAGNI MAD.
def string_to_int(word):
    char_map = {
        '0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
        '6':6, '7':7, '8':8, '9':9
    }
    number = 0

    for char in word:
        string_digit = char_map[char]
        number = (number * 10) + string_digit
    return number


number1 = 3     # example of YAGNI being ignored.
number2 = 6     # making more variable than needed, or not putting into a list
number3 = 8     # or not asking the user for numbers
number4 = 2
number5 = 5
number6 = 9

print(add(number6, number5))