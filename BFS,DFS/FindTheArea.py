import sys
sys.stdin = open("../input.txt","r")

"""
    M , N ,K <= 100
    
    x,y
    왼쪽 아래 꼭지점 (0,0), 오른쪽 위 꼭지점 (N,M)
"""
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(area,x,y):
    cnt =1
    stack = []
    stack.append((x,y))
    area[y][x] = 1

    while stack:
        cx , cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < len(area[0]) and 0 <= ny < len(area):
                if area[ny][nx] == 0:
                    cnt += 1
                    area[ny][nx] = 1
                    stack.append((nx,ny))
    return cnt


M,N,K = map(int,input().split())

area = [[0 for _ in range(N)] for _ in range(M)]



for _ in range(K):
    lbx , lby , rtx , rty = map(int,input().split())
    for x in range(lbx,rtx):
        for y in range(lby, rty):
            area[y][x] = 1
result =[]
for i in range(N):
    for j in range(M):
        if area[j][i] == 0:
            result.append(dfs(area,i,j))

result =sorted(result)

print(len(result))
for v in result:
    print(v ,end=' ')



