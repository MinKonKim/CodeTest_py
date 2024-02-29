# https://www.acmicpc.net/problem/1522
import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

# a의 갯수를 센다
# a의 갯수만큼의 길이로 문자열을 슬라이싱한다
# 슬라이싱된 문자열에서 b 의 갯수를 센다
# 카운팅 된 b만 교환해 주면 되므로, b의 갯수 == 교환 횟수
# 문자열을 순회하며, b의 갯수를 세면서 최솟값을 찾으면 된다. 

# 입력 받기
s = input()

a = s.count('a')
s+= s[0:a-1]
min_val = float('inf')
for i in range(len(s)-(a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)


