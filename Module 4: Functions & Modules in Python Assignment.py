'''Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

x = input('Enter the value to find the factorial function: ')
x = int(x)
result = factorial(x)
print(f'The factorial of {x} is: ', result)

'''Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''

import math
y = input('Enter a number: ')
y = int(y)

#square root
square = math.sqrt(y)
print('Square root: ', square)

# logarithms
log = math.log(y)
print('Logarithm: ', log)

#sine of the number
sin = math.sin(y)
print('Sine: ', sin)
