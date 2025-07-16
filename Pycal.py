import main

a = input("Enter first number: ")
b = input("Enter second number: ")

OP = input("Enter operation add, sub, mul, div: ")

if OP == "add":
    result = main.addition(int(a), int(b))
    print(f"Result: {result}")

elif OP == "sub":
    result = main.subtraction(int(a), int(b))
    print(f"Result: {result}")

elif OP == "mul":
    result = main.multiplication(int(a), int(b))
    print(f"Result: {result}")

elif OP == "div":
    result = main.division(int(a), int(b))
    print(f"Result: {result}")

else:
    print("Invalid operation. Please choose add, sub, mul, or div.")