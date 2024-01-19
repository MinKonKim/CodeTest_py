import sys
sys.stdin = open("../input.txt","r")

"""

처음 두 물통은 비어있고 , 마지막만 가득차있다.

옮겨담기를 진행,

A,B,C 의 물통중에서 하나라도 완전히 비거나 가득차면 종료,
                            
첫번째 물통이 비어 있을 때, 세 번째 물통에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성

즉 ,경우의 수를 모두 구해야한다.

출력 오름차순으로 정렬

"""
def move_water(x,y,z,a,b,c):
    # 물통 A에서 B로 물을 옮기는 경우
    yield (x - min(x, b - y), y + min(x, b - y), z)

    # 물통 B에서 A로 물을 옮기는 경우
    yield (x + min(y, a - x), y - min(y, a - x), z)

    # 물통 B에서 C로 물을 옮기는 경우
    yield (x, y - min(y, c - z), z + min(y, c - z))

    # 물통 C에서 B로 물을 옮기는 경우
    yield (x, y + min(z, b - y), z - min(z, b - y))

    # 물통 A에서 C로 물을 옮기는 경우
    yield (x - min(x, c - z), y, z + min(x, c - z))

    # 물통 C에서 A로 물을 옮기는 경우
    yield (x + min(z, a - x), y, z - min(z, a - x))

def dfs():
    result=[]
    stack =[(0,0,C)]
    visited = [[False]*(C+1)for _ in range(C+1)]
    while stack:

        x,y,z = stack.pop()
        if x ==0 and z not in result:
            result.append(z)
        for nx,ny,nz in move_water(x,y,z,A,B,C):
            if not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx,ny,nz))

    return sorted(result)

A,B,C = map(int, input().split())

print(*dfs())