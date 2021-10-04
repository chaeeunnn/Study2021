import sys

T = int(sys.stdin.readline()) #테스트개수 입력
for i in range(0,T):
    N,M = map(int, sys.stdin.readline().split()) #국가수와 비행기종류 입력
    for j in range(0,M):
        a,b = list(map(int,sys.stdin.readline().split()))
    print(N-1) #연결그래프이므로 방문횟수와 상관없이 '비행기종류'는 N-1