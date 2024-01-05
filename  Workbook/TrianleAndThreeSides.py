import sys

sys.stdin = open("../input.txt","r")


while True:

    sides = list(map(int, input().split()))
    if sides[0] ==0:
        break
    longestSide = max(sides)
    sides.remove(longestSide)

    if longestSide >=sum(sides):
        print("Invalid")
        continue
    else :
        sides.append(longestSide)

    if sides[0] == sides[1] and sides[1] == sides[2]:
        print("Equilateral")
    elif  sides[0] != sides[1] and sides[1]!=sides[2] and sides[0] != sides[2]:
        print("Scalene")
    else:
        print("Isosceles")


