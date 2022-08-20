"""
Write a function that inputs a number and prints the multiplication table of that number
"""
def multiply_table(n):
    for i in range(11):
        multiply_numbers = n * i
        print("The multiplication table of {0} * {1} is =".format(n, i), n * i)

multiply_table(3)