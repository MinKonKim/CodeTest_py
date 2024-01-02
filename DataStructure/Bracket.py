import sys
sys.stdin  = open("../input.txt","r")


N = int(input())

for _ in range(N):
    stack = []
    st  = input()
    for c in st:
        if c =='(':
            stack.append(1)
        else :
            if stack:
                stack.pop()
            else :
                stack.append(1)
                break
    if  stack:
        print("NO")
    else :
        print("YES")