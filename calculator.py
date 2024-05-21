def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
5
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Select operation:")
print("+. Add")
print("-. Subtract")
print("*. Multiply")
print("/. Divide")

choice = input("Enter choice (+,-,*,/): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")