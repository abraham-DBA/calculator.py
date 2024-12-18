operator = input("Select an operator to use(+ , * , - , /)")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "+":
    answer = num1 + num2 
    print(f"The answer for the Addition of {num1} and {num2} is {answer} ")
elif operator == "*":
    answer = num1 * num2
    print(f"The answer for the Multiplication of {num1} and {num2} is {answer} ")
elif operator == "-":
    answer = num1 - num2
    print(f"The answer for the Subtraction of {num1} and {num2} is {answer} ")
elif operator == "/":
    answer = num1 / num2
    print(f"The answer for the Division of {num1} and {num2} is {answer} ")
else:
    print("Enter a valid Operator please")        