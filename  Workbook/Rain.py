#빗물
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

H, W = map(int, input().split())
blocks = list(map(int,input().split()))

div2=[[0 for _ in range(W)]for _ in range(H)]

for i in range(W):
    b = blocks[i]
    for j in range(H-1, H-1-b ,-1):
        div2[j][i] = 1

result =0

for i in range(H):
    stack =[]
    isCan = False
    for j in range(W):
        if div2[i][j] == 1 and isCan:
            result += len(stack)
            stack.clear()
            isCan= False
        elif div2[i][j] == 1 and len(stack) == 0:
            isCan = True
        elif div2[i][j] == 0:
            stack.append(1)
print(result)