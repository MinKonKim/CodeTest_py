import sys,copy  
input=sys.stdin.readline  
from collections import deque  

#유니온-파인드 알고리즘
# input.txt
# 4 3
# 1 2 3
# 2 3 2
# 2 4 4
# 1 2
# 4 1
# 3 1
def Find(x): # 유니온 파인드의 Find 함수 : x의 루트를 찾아가는 함수.

    # disjoint : 여러 개의 원소가 각각 속한 집합을 표현하기 위한 배열
    # 이 배열의 인덱스는 원소, 값은 해당 원소가 속한 집합의 대표 원소(루트)를 의미한다.
    # 즉, disjoint[i] 는 원소 i 가 속한 집합의 대표 원소를 가리킨다.
    # 왜 사용하나?
    # 두 원소가 같은 집합에 속하는지 여부를 빠르게 판단하거나, 두 집합을 합치는 등의 작업을 효율적으로 수행가능함.

    #  if x == disjoint[x] : x 가 집합의 대표 원소인지 확인하는 부분,
    if x!=disjoint[x]:  #disjoint[x] : x의 부모 원소
        disjoint[x] = Find(disjoint[x])  # 경로 압축을 수행하는 부분 : x와 x의 부모를 바로 연결
    return disjoint[x]

def Union(a,b): # 유니온 파인드의 Union 함수  
    a=Find(a) ; b=Find(b)  

    if a==b:  
        return  
    if a>b:  
        disjoint[a]=b  
        dp[b]+=dp[a]  
    else:  
        disjoint[b]=a  
        dp[a]+=dp[b]  

N,Q=map(int,input().split())  

graph=[] # 트리를 저장할 그래프를 선언한다.  
dp=[1]*(N+1)  

for i in range(N-1):  
    a,b,c=map(int,input().split())  
    graph.append((a,b,c))  

graph.sort(key=lambda x:-x[2])  # c를 기준으로 내림차순 정렬
graph=deque(graph)  
L=[ list(map(int,input().split())) for _ in range(Q) ] # 쿼리를 입력받는다.  
Query=copy.deepcopy(L) # 쿼리를 미리 복사한다.  

L.sort(key=lambda x:-x[0]) # k 값이 높은 순서대로 정렬한다.  
disjoint=[ i for i in range(N+1) ] # 분리집합을 위한 배열을 만든다.  

D={} # 오프라인 쿼리를 위한 딕셔너리  
for K,V in L: # 쿼리 실행.  
    while graph and graph[0][2]>=K:  
        if Find(graph[0][0])!=Find(graph[0][1]):  
            Union(graph[0][0] , graph[0][1])  
            graph.popleft()  
    D[(K,V)] = dp[Find(V)]-1  


for K,V in Query: # 이전의 복사해둔 쿼리를 사용한다.  
    print(D[(K,V)]) # 그때의 딕셔너리 값을 출력한다.