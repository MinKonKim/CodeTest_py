# heap정렬 이해하고 오기
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

import heapq

# 입력 받기
n = int(input())

# 최소힙 초기화
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(min_heap,num)
    else:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)

