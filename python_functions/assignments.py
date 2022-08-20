"""
1. Write a function that inputs a number and prints the multiplication table of that number
"""
def multiply_table(n):
    range_of_number = int(input("Enter the range of number to be multipled: "))
    for i in range(1, range_of_number+ 1):
        print("The multiplication table of {0} * {1} is =".format(n, i), n * i)

multiply_table(3)

"""
Write a program to print twin primes less than 1000. If two consecutive odd numbers are
both prime then they are known as twin primes
"""

