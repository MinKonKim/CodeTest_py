import sys
sys.stdin = open("../input.txt","r")

N= int(input())
times = list(map(int, input().split()))

times = sorted(times)

total =0
time = 0
for i in range(N):
    total += times[i]
    time += total

print(time)