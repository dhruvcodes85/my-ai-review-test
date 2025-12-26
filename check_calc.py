# A simple calculator for my student project
import os

def calculate():
    print("--- Simple Python Calculator ---")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    expression = f"{num1} {op} {num2}"
    result = eval(expression)


    print(f"Result: {result}")

def run_system_command():
    
    os.system("echo Calculator is running")

calculate()