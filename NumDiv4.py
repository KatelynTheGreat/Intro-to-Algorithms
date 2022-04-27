
import math


test = input("Type num")
check = 0
total = 0

x = [int(a) for a in str(test)]
print(x)


while(check < len(x)):
    total = total + x[check]
    check += 1




def checkDivFour():
    a = test
    a_string = str(a)
    a_length = len(a_string)
    c = int(a_string[a_length - 2: a_length])
    d = c/4
    print(d)

    if d.is_integer():
        print("TIS NICE")

checkDivFour()

