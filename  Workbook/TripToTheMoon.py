#진우의 달 여행
import sys
sys.stdin = open("../input.txt","r")
INF = float('inf')

N,M = map(int, input().split())

fuels = [list(map(int,input().split())) for _ in range(N)]
# 3차원
dp = [[[0]*3 for _ in range(M)]for _ in range(N)]

#dp 초기화
for j in range(M):
    for k in range(3):
        dp[0][j][k] = fuels[0][j]

#solution
for i in range(1,N):
    for j in range(M):
        for k in range(3):
            # 왼쪽 아래 방향으로 갈때, 갈 수 없는 상황 or 오른쪽 아래로 갈 때, 갈 수 없는 상황
            if (j == 0 and k ==0 )or (j == M-1 and k==2):
                dp[i][j][k] = INF
                continue
            if k == 0:  # 왼쪽 아래 방향 일 때
                dp[i][j][k] = fuels[i][j] + min(dp[i-1][j-1][1],dp[i-1][j-1][2])
            elif k == 1: # 아래 방향 일 때
                dp[i][j][k] = fuels[i][j] + min(dp[i-1][j][0],dp[i-1][j][2])
            else : # 오른쪽 아래 방향 일 때
                dp[i][j][k] = fuels[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

result = INF
# 연료의 최소비용 찾기
for j in range(M):
    # result = min(result, dp[마지막][0~M-1]에 있는 숫자들 중 가장 작은 값 )
    result = min(result,min(dp[-1][j]))

print(result)


