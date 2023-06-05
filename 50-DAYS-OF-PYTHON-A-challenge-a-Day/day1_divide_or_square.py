"""
##Day 1: Division and Square-root###
Write a function called divide_or_square that takes one
argument (a number), and returns the square root of the number
if it is divisible by 5, returns its remainder if it is not divisible by
5. For example, if you pass 10 as an argument, then your function
should return 3.16 as the square root.

###Extra Challenge: Longest Value###
Write a function called longest_value that takes a dictionary
as an argument and returns the first longest value of the
dictionary. For example, the following dictionary should return
– apple as the longest value.
fruits = {'fruit': 'apple', 'color': 'green'}
"""

def divide_or_square(number):
    if number % 5 == 0:
        sq_root = number ** 0.5
        return f'the square-root of the number is {sq_root}'
    else:
        remainder = number % 5
        return f'The remainder of the division is {remainder}'

number = int(input("write a int numer: "))
print(divide_or_square(number))