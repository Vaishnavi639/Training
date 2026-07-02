is_rich = True
is_independent = True
if is_rich and is_independent:
    print("Great")
elif is_rich and not(is_independent):
    print("Dependency issues")
elif not(is_rich) and is_independent:
    print("Strong")
else:
    print("Liability")


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(num1, " is the largest")
    elif num2>=num1 and num2>=num3:
        print(num2," is the largest")
    else:
        print(num3," is the largest number")

max_num(3,4,6)