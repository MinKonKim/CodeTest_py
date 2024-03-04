#  영단어 암기는 어려워,  pypy3로 제출시 정답.

import sys
sys.stdin = open('C:\\CodeTest_py\\input.txt', "r")
input = sys.stdin.readline
from collections import defaultdict

count = {i:[] for i in range(1,100001)}
words = defaultdict(int)
n,m = map(int,input().split())
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else:
        words[word] +=1

for i in words:
    count[words[i]].append(i)

for j in range(n,0,-1):
    if count[j]:
        # x의 길이가 긴 순서로 정렬하되, 길이가 같은 경우에는 x의 알파벳 순서로 정렬
        count[j].sort(key = lambda x:(-len(x),x))
        print(*count[j],sep='\n')