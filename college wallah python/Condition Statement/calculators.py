# num1 = int(input("Enter number1:"))
# num2 = int(input("Enter number2: "))

# operator = input("Enter operators: ")

# match operator:
#     case "+":
#         print("sum is", num1 + num2)
#     case "-":
#         print("Difference is", num1 - num2)
        
#     case "*":
#         print("product is", num1 * num2)
        
#     case "/":
#         print("Division is", num1 / num2)
        
#     case "%":
#         print("percentage is", num1 % num2)
        
#     case "**":
#         print("power is", num1 ** num2)
        
#     case _ :
#         print("Enter valid operators: ")    




# Engineering calculators
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Sine")
    print("8. Cosine")
    print("9. Logarithm (base 10)")
    print("10. Exit")

    choice = input("Enter choice (1-10): ")

    if choice == '10':
        print("Exiting the calculator.")
        break

    if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Invalid input. Please enter a valid option.")
        continue

    num1 = float(input("Enter first number: "))

    if choice in ('5', '6', '7', '8', '9'):
        if choice == '5':
            print(f"Square root of {num1} = {math.sqrt(num1)}")
        elif choice == '6':
            exponent = float(input("Enter exponent: "))
            print(f"{num1} ^ {exponent} = {math.pow(num1, exponent)}")
        elif choice == '7':
            print(f"Sine of {num1} = {math.sin(math.radians(num1))}")
        elif choice == '8':
            print(f"Cosine of {num1} = {math.cos(math.radians(num1))}")
        elif choice == '9':
            print(f"Logarithm (base 10) of {num1} = {math.log10(num1)}")

    else:
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")


