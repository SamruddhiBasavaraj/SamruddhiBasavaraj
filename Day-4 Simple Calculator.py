# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
print(" % for modulus")
print("// for floor division")
print("** for exponent")

choice = input("Enter operator: ")

if choice == "+":
    print("Result =", num1 + num2)

elif choice == "-":
    print("Result =", num1 - num2)

elif choice == "*":
    print("Result =", num1 * num2)

elif choice == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
        
if choice == "%":
    print("Result =", num1 % num2)

elif choice == "//":
    print("Result =", num1 // num2)

elif choice == "**":
    print("Result =", num1 ** num2)

else:
    print("Invalid operator!")