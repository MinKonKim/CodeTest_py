import sys
sys.stdin = open("../input.txt","r")

batch = input()

stack =[]
last= None
result = 0
for ch in batch:
    if ch =='(':
        stack.append(ch)
    else :
        stack.pop()
        if last =='(':
            result += len(stack)
        else :
            result +=1

    last = ch
print(result)

