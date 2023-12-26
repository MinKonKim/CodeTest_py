import sys
sys.stdin = open("../input.txt", "r")

def max_subarray_sum(arr):
    max_sum = float('-inf')  # 최댓값을 음의 무한대로 초기화
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# 입력 처리
n = int(input())
sequence = list(map(int, input().split()))

# 최대 연속 부분합 구하기
result = max_subarray_sum(sequence)

# 결과 출력
print(result)
