
import math


test = input("Type num")
check = 0
total = 0

x = [int(a) for a in str(test)]
print(x)


while(check < len(x)):
    total = total + x[check]
    check += 1


def checkDivThree():

    isdivby3 = total/3

    if isdivby3.is_integer():
        print("TIS NICE")

    print(total/3)

checkDivThree()

