import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

def dfs():
    stack =[1]
    visited = [False for _ in range(N+1)]
    visited[1] = True
    cnt = 0
    while stack :
        cur = stack.pop()
        for i in graph[cur]:
            if not visited[i]:
                stack.append(i) 
                visited[i] = True
                cnt+=1
    return cnt


N = int(input())
M = int(input())

graph = [[]for _ in range(N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

print(dfs())