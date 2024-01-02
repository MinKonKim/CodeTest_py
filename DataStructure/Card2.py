import sys
sys.stdin = open("../input.txt","r")

from collections import deque

N = int(input())
queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()  # 제일 위의 카드를 버림
    queue.append(queue.popleft())  # 그 다음 카드를 제일 아래로 옮김

print(queue[0])  # 마지막으로 남은 카드를 출력



