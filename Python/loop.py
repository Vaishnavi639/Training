def power_of(base,power):
    result=1
    for i in range(power):
        result=result*base
    return result

print(power_of(4,18))