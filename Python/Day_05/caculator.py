# Command Line Args 
# Package used for command line arg is "sys"
# Arguments are accesses using "argv" variables
import sys
import os

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 // num2

print("Addition: ", addition(num1, num2))
print("Subtraction: ", subtraction(num1, num2))
print("Multiplication: ", multiplication(num1, num2))
print("Division: ", division(num1, num2))

print(os.getenv("password"))
print(os.getpid)