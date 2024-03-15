import sys
sys.stdin = open('../input.txt', "r")
#  Qu 0.25 Di 0.10 Ni 0.05 Pe 0.01
# =>   25       10       5       1
def calCoins(Money):
   Qu =0
   Di =0
   Ni =0 
   Pe =0
   if (Money >= 25):
       Qu = Money//25
       Money -= Qu*25
   if (Money >= 10):
       Di = Money//10
       Money -= Di*10
   if (Money >= 5):
       Ni = Money//5
       Money -= Ni*5
   if (Money >= 1):
       Pe = Money

   print(Qu, Di, Ni, Pe)
        




T = int(input())

for _ in range(T):
    Money = int(input())
    calCoins(Money)

