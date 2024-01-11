import sys
sys.stdin = open("../input.txt","r")

"""
 - 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
 - N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
 - i번 집의 색은 i-1, i+1 번의 색과 같지 않아야 한다.
"""

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

result = float('inf')  # 최솟값을 저장할 변수를 초기화

for first in range(3):  # 첫 번째 집의 색을 선정
    dp = [[0]*3 for _ in range(n)]
    for i in range(3):
        if i == first:
            dp[0][i] = costs[0][i]
        else:
            dp[0][i] = float('inf')

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for i in range(3):
        if i == first:  # 마지막 집의 색이 첫 번째 집의 색과 같으면 skip
            continue
        result = min(result, dp[n-1][i])  # 최솟값 업데이트

print(result)





