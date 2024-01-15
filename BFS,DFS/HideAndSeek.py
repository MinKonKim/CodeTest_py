from collections import deque

def bfs(Diagram, root):
    visited = [False]*(len(Diagram)+1)
    distance = [0]*(len(Diagram)+1)
    queue = deque([root])

    visited[root] = True
    while queue:
        vertex = queue.popleft()

        for next in Diagram[vertex]:
           if not visited[next]:
               queue.append(next)
               visited[next] = True
               distance[next] = distance[vertex]+1

    return distance

N, M = map(int, input().split()) # N : 헛간갯수 , M : 연결 선의 수
Diagram = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    Diagram[A].append(B)
    Diagram[B].append(A)

distance = bfs(Diagram, 1)
max_dist = max(distance)
print(distance.index(max_dist), max_dist, distance.count(max_dist))
