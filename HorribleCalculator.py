
def add(numb1, numb2):
    num1 = numb1          # KISS: There's no need to assign to new variable.
    num2 = numb2
    total = 0
    total = total + num1
    total = total + num2    # DRY: same function can be condensed into one.
    return total

def subtract(numb1, numb2):
    number = numb1
    number += numb2               # DRY: Repeated steps that could have been put into one line.
    return number - (numb2 * 2)   # KISS: more complicated than it needs to be, too many unneeded steps

def multiply(numb1, numb2):
    multiplied_number_after_for_loop = numb1
    for i in range(numb2):
        multiplied_number_after_for_loop += numb1
    multiplied_number_after_for_loop -= numb1
    return multiplied_number_after_for_loop         # KISS: too many steps, using code to correct incorrect code logic

# The below method is my favorite deviation of KISS.
def divide(numb1, numb2):
    working_calculation = numb1
    count = 0
    decimal = 0

    while working_calculation > numb2:
        working_calculation -= numb2
        count += 1

    if working_calculation > 0:
            decimal += (working_calculation * 10) / numb2
            count += decimal / 10

    return count

# YAGNI: absolutely unnecessary method. User can just enter ints, or we can typecast strings on request.
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


number1 = 3     # YAGNI:
number2 = 6     # making more variable than needed, or not putting into a list
number3 = 8     # or not asking the user for numbers
number4 = 2
number5 = 5
number6 = 9

print(add(number6, number5))
print(subtract(number6, number5))
print(multiply(number6, number5))
print(divide(number6, number5))