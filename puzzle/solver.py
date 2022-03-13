# Given 2 intergers, find the sum of all the numbers between them (inclusive).
# If the two intergers are equal, return a string: "Cannot add".

def add_numbers(num1, num2):
    if num1 == num2:
        return "Cannot add"
    else:
        return sum(range(num1, num2 + 1))