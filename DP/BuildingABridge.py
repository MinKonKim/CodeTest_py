import sys
sys.stdin = open('C:\CodeTest_py\input.txt', "r")

# 동적 계획법을 사용한 이항 계수 계산 함수
def build_bridges(n, k):
    if k == 0 or n == k:
        return 1
    if dp[n][k] != -1:
        return dp[n][k]
    dp[n][k] = build_bridges(n - 1, k - 1) + build_bridges(n - 1, k)
    return dp[n][k]

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대한 다리 건설 결과 출력
for _ in range(T):
    N, M = map(int, input().split())
    
    # 동적 계획법을 위한 배열 초기화
    dp = [[-1] * (M + 1) for _ in range(M + 1)]
    # 경우의 수 계산
    result = build_bridges(M, N)
    print(dp)
    print(result)
