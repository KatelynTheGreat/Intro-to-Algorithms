
import math


test = input("Type num")
check = 0
total = 0

x = [int(a) for a in str(test)]
print(x)


while(check < len(x)):
    total = total + x[check]
    check += 1



def checkDivsev():
    a = test
    sev = int(str(a)[:2])
    mathit = sev - 1 * 5
    if mathit.is_integer():
        print("TIS NICE")
    print(mathit)



checkDivsev()