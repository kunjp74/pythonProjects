num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator(+, -, *, /): ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2) 
elif op == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1 / num2)