import sys
sys.stdin = open("../input.txt","r")
"""
    1 땅 0 바다
"""

dirX = [0,0,1,1,1,-1,-1,-1]
dirY = [1,-1,0,1,-1,0,1,-1]

def dfs(y,x):
    visited[y][x] = True
    stack =[(y,x)]
    while stack:
        (cy,cx)= stack.pop()
        for i in range(8):
            ny = cy+dirY[i]
            nx = cx+dirX[i]
            if ny >= 0 and nx >= 0 and ny <h and nx <w and islands[ny][nx]  == 1 and not visited[ny][nx]:
                stack.append((ny,nx))
                visited[ny][nx] = True
    return  1

while True:
    islands= []
    cnt = 0
    w,h= map(int,input().split())

    if w == 0 and h == 0:
        break

    for _ in range(h):
        islands.append(list(map(int ,input().split())))

    visited = [[False for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if not visited[y][x] and islands[y][x] ==1:
                cnt+=dfs(y,x)
    print(cnt)

