output = 0
num1 = ""
operation = ""
num2 = ""


num1 = input(" Enter First Number: ")
operation = input("Operation (+, -, *, /)\n")
num2 = input("Enter Second Number: ")

floatnum1 = float(num1)
floatnum2 = float(num2)


if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
    print("Your Answer: "+str(output))
else:
    print("Your operation is invalid, please try again")