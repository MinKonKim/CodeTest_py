import sys

sys.stdin =open("../input.txt","r")


def josephus(n, k):
    # 1부터 n까지의 숫자를 넣은 리스트 생성
    circle = list(range(1, n+1))
    result = []  # 결과를 저장할 리스트
    index = 0  # 시작 인덱스

    while circle:
        index = (index + k - 1) % len(circle)  # 제거할 요소의 인덱스 계산
        result.append(circle.pop(index))  # 요소를 제거하고 결과 리스트에 추가

    return result

n, k = map(int, input().split())  # N과 K 입력
result = josephus(n, k)  # 요세푸스 순열 계산

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")
