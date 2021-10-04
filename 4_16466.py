N = int(input()) #팔린 티켓의 수
arr = list(map(int, input().split())) #팔린 티켓들의 번호
arr.sort() # 팔린티켓번호 오름차순 정렬
ticket = 1 #가질 수 있는 티켓 번호 1로 초기화
for i in arr : #정렬된 리스트를 처음부터 탐색하며
    if ticket < i : #팔린티켓번호보다 작으면 
        print(ticket) #출력 후 반복문 탈출
        break
    ticket += 1 #티켓에 1씩 더하면서 비교

if ticket > arr[-1] : # 예를 들어 팔린 티켓이 1 2 3 4 5 면 가질 수 있는 티켓 번호 6
    print(arr[-1]+1)
