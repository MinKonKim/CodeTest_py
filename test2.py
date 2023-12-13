import sys
sys.stdin = open("input.txt", "r")

TC = int(input())

# 주차요금 = 차량의 무게 * 주차공간 마다 따로 책정된 무게당 금액액

for tc in range(1,TC+1):
   D,A,B,F = map(int, input().split())

   result = F * (D//(A+B))

   print(f"#{tc} {result}")
