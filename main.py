#TODO Calculator FUNCTIONS

def calculate(num1, num2, operation):
        if operation == "*" or "x" or "X":
                result=num1 * num2
                return result
        #TODO (CONTINUE ON THE SAME PATTERN




num1 = int(input("Enter 1st number: "))#TODO INPUT FROM USER
num2 = int(input("Enter 2nd number: "))#TODO INPUT FROM USER
op = input("Enter your opration: ")#TODO INPUT FROM USER
print(calculate(num1, num2, op))