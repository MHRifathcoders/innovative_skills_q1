"""Q.2 You are building a calculator app. Write a Python function calculate() that takes two
numbers and an operator (+, -, *, /) as input and returns the result."""

def calculate(user_number1, user_number2, user_operator):
    if user_operator == "+":
        return user_number1 + user_number2
    elif user_operator =="-":
        return user_number1 - user_number2
    elif user_operator =="*":
        return user_number1 * user_number2
    elif user_operator == "/":
        if user_number2 == 0:
            return "Error, 0 can not divisible"
        return user_number1 /user_number2
    else:
        return "Invalid Operator you Choose"
try:      
    user_number1= int(input("Enter your number: "))
    user_number2= int(input("Enter your number: "))
    user_operator= input("Enter the operator (+, -, *, /): ")
    if user_operator not in ["+","-","*","/"]:
        print("Error; inavlid operator, please use Enter the operator (+, -, *, /)")
    else:
        result= calculate(user_number1, user_number2, user_operator)
        print(result)
except ValueError:
    print("Ivalid input, please input valid number")
