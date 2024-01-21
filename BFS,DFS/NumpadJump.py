import sys
sys.stdin = open("../input.txt","r")

dirX = [1,0,-1,0]
dirY = [0,1,0,-1]

def dfs(number, x,y):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return
    number+= numpad[y][x]
    for i in range(4):
        nx = x +dirX[i]
        ny = y+ dirY[i]
        if nx <5 and ny <5 and nx >=0 and ny>= 0:
            dfs(number,nx,ny)



numpad = []

for _ in range(5):
    numpad.append(list(map(str,input().split())))
    result =[]

for i in range(5):
    for j in range(5):
        dfs('',i,j)

print(len(result))