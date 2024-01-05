import sys
sys.stdin = open("../input.txt","r")

world = input().upper()

alphabets={}

for char in world:
    if char not in alphabets:
        alphabets[char] = 1
    else :
        alphabets[char] +=1

max_value = max(alphabets.values())

max_keys = [k for k , v in alphabets.items() if v == max_value]

if len(max_keys) >1 :
    print("?")
else :
    print(max_keys[0])



