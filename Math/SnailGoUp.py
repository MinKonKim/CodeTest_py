import sys
sys.stdin = open("../input.txt","r")

import math

A,B,V = map(int, input().split())


dayDist = A-B

days = math.ceil((V-B)/(A-B))

print(days)