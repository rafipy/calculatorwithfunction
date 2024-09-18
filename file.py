import math

def calculate(num1, num2, oper):
    if oper == "+" :
        return(num1 + num2)
    if oper == "-":
        return(num1 - num2)
    if oper == "/":
        return(num1 / num2)
    if oper == "*":
        return(num1 * num2)

# def clear(answer):
#     answer.lower()
#     if answer == "clear":
#         return answer == ""


answer = int(input("Input the first Number"))
no2 = int(input("insert the Next Number"))
op = input("Insert an Operator")
print(calculate(answer, no2, op))