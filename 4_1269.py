N, M = map(int, input().split()) # N:A의 원소개수, M:B의 원소개수
#set(집합) 자료형 이용
# - 합집합 : A|B
# - 교집합 : A&B
# - 차집합 : A-B
A = set(map(int, input().split())) 
B = set(map(int, input().split()))

#대창차집합 : (A-B)와 (B-A)의 합집합
print(len((A-B)|(B-A)))
#대칭차집합 = A+B-2*(AnB)
#print(len(A)+len(B)-2*len(A&B)) # A&B : A와 B의 교집합

#시간초과
#count = 0
# for i in A_element :
#     for j in B_element :
#         if i == j :
#             count += 1
#print(len(A_element)+len(B_element)-2*count)