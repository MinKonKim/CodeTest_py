import sys

def makeNumber(num):

    if num <10:
        return num*2;
    str_num = str(num)
    total = 0

    for char in str_num:
        total += int(char)
    return num+total

numbers = [False]*10001

for n in range(1,9994):
    num = n
    while num < 10001:
        num = makeNumber(num)
        if num < 10001 :
            if not numbers[num] :
                numbers[num] = True
            else :
                break

for i in range(1,10001):
    if not numbers[i]:
        print(i)

   
    




