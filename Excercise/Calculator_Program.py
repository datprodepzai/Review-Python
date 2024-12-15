num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

operator = input("Enter an Operator(+ , - , * , /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is not a valid operator !")

print(f"Result = {result}")
