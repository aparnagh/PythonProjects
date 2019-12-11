'''
Created on August 28, 2019

@author: Aparna Ganesh
'''
import math
import random
from numpy.matlib import rand


def calculator():
    print("List of operations: ")
    print("Enter 'add' for the addition of numbers")
    print("Enter 'subtract' for the subtraction of numbers")
    print("Enter 'multiply' for the product of numbers")
    print("Enter 'divide' for the division of numbers")
    print("Enter 'quit' to exit the calculator")
    print("Enter 'more' for additional operations")

    userInput = input("Enter operation desired")
    notQuit = True

    while notQuit:
       
        if userInput == "quit":
            notQuit = False
                 
        elif userInput == "more":
            print("Enter 'sin' to find sine of the number")
            print("Enter 'cos' to find the cosine of the number")
            print("Enter 'tan' to find the tangent of the number")
            print("Enter 'power' to find the value of a number raised to another number")
            print("Enter 'random' to get a random number between two specified numbers")
            continue
        
        elif userInput == "add":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                summ = str(num1 + num2)
                print(summ)
                calculator()
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
                
        elif userInput == "subtract":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                diff = str(num1 - num2)
                print(diff)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
                
        elif userInput == "multiply":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                product = str(num1 * num2)
                print(product)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
                
        elif userInput == "divide":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                sum = str(num1 + num2)
                print(sum)
                break
            except ZeroDivisionError:
                print("Error - Divisor Cannot Be 0")
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
                
        elif userInput == "sin":
            try:
                num = float(input("Enter the number: "))
                result = str(math.sin(num))
                print(result)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Value")
        
        elif userInput == "cos":
            try:
                num = float(input("Enter the number: "))
                result = str(math.cos(num))
                print(result)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Value")
        
        elif userInput == "tan":
            try:
                num = float(input("Enter the number: "))
                result = str(math.tan(num))
                print(result)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Value")
                
        elif userInput == "power":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = str(num1 ** num2)
                print(result)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
        
        elif userInput == "random":
            try:
                num1 = float(input("Enter the lower bound of the random number: "))
                num2 = float(input("Enter the upper bound of the random number: "))
                rand = str(random.randint(num1, num2))
                print(rand)
                break
            except(ValueError, TypeError):
                print("Error - Please Enter Valid Values")
                
        else:
            print("Try Again")

