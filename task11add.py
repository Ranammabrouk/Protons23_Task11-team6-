def perform_addition():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
    print("The sum is:", result)
operation = input("Select an operation (1 for addition): ")
if operation == "1":
    perform_addition()
