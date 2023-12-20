def max_score(stairs):
    # 계단의 개수
    n = len(stairs)

    # 계단의 개수가 1개일 때, 첫 번째 계단 점수가 최댓값
    if n == 1:
        return stairs[0]

    # 계단의 개수가 2개일 때, 두 번째 계단 점수가 최댓값
    if n == 2:
        return max(stairs[0] + stairs[1], stairs[1])

    # dp[i]: i번째 계단까지의 최대 점수
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = max(stairs[0] + stairs[1], stairs[1])

    # 세 번째 계단부터 계산 시작
    for i in range(2, n):
        # i번째 계단까지 올라오는 경우의 수는
        # (i-2번째 계단까지 올라왔을 때 최대값 + 현재 계단의 점수) 또는
        # (i-3번째 계단까지 올라왔을 때 최대값 + 이전 계단의 점수 + 현재 계단의 점수) 중 큰 값을 선택
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    # 마지막 계단까지 올라왔을 때 최대값 반환
    return dp[-1]


# 입력 받기
n = int(input())  # 계단의 개수
stairs = []
for _ in range(n):
    stairs.append(int(input()))  # 각 계단의 점수 입력받기

# 최대 점수 출력
print(max_score(stairs))
