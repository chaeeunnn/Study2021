#블랙잭

import sys
input = sys.stdin.readline
#카드 개수,합 입력
N,M = map(int,input().split())
#카드에 쓰여있는 수 리스트에 입력받기
# arr=[input() for _ in range(N)]
arr = list(map(int, input().split()))

sum = 0
min = M
ans = 0
#카드의 합, 한도와 합의 차이< = 0
#세 개의 카드를 선택할 수 있는 경우를 모두 탐색
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = arr[i] + arr[j] + arr[k]
            if sum > M:
                continue
            elif M - sum <= min: #합과 한도값의 차이가 최소가 되는 경우
                min = M - sum
                ans = sum

print(ans)