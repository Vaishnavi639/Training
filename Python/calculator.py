num1 = float(input("Enter a numner: "))
op=input("Enter operator: ")
num2 = float(input("Enter a number: "))

if op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
else:
    print("invalid operator")