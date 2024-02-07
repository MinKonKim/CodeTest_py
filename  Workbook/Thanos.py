import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")

S = input()

oneCnt , zeroCnt = 0,0

for i in range(len(S)):
    if S[i] == '1':
        oneCnt +=1
    else:
        zeroCnt += 1

print(oneCnt,zeroCnt)