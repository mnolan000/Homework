"""
File: HW6.py
Author: Matthew Nolan
Date: 2/24/25
Description: Program that asks for 2 numbers, then returns 4 arthimetic operations
"""

#ask the user for inputs for 2 numbers
number1 = input("Number 1? ")
number2 = input("Number 2? ")

#print the operations
print(f"{number1} + {number2} = {int(number1)+int(number2)}")
print(f"{number1} - {number2} = {int(number1)-int(number2)}")
print(f"{number1} * {number2} = {int(number1)*int(number2)}")
print(f"{number1} / {number2} = {int(number1)/int(number2)}")

