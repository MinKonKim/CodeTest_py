#택배 배송

import sys 
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")
import heapq

def dijkstra(graph, start):
    distances = [float('inf') for _ in range(len(graph))]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

distances = dijkstra(graph, 1)
print(distances[N])
