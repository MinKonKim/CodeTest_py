import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")
# 테두리가 6의 배수 만큼 증가.

N = int(input())
total = 1
i = 1

while total <N:
    total += 6*i
    i += 1
    print(total)
    
print(i)