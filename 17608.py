import sys
input = sys.stdin.readline
N=int(input())
height=[input() for _ in range(N)]
height=list(map(int,height))
top=height[N-1]
count=0
for i in range(N-1,-1,-1):
    if top < height[i]:
        count+=1
        top=height[i]
print(count+1)