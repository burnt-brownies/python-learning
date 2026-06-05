# =================================================
# Python Basics - Numeric Data (Integers & Floats)
# =================================================

num = 3
print(type(num)) # returns that num belongs to class integer

num = 3.14
print(type(num)) # type is float

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

num = 1 

# incrementing
num = num + 1
print(num)

num += 1
print(num)

num *= 10
print(num) 

# absolute value
print(abs(-3))

# rounding off
print(round(3.75))
print(round(3.75 , 1)) # round to 1st digit after the decimal

# Comparisons: (return boolean true / false values)
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num1 = 3 
num2 = 2

print(num1 == num2)
print(num1 != num2)

# they are strings, not numbers
number1 = '100'
number2 = '200'

print(number1 + number2) # we dont get the result we wanted, we get 100200, concatenation

# to turn the numbers into integers we need casting
number1 = int(number1)
number2 = int(number2)