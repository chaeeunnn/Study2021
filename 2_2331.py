n=int(input())
ans = 0 #해를 못 찾았을 경우 0
for i in range(n):
    s = str(i) #각 자리수를 index로 접근하기 위함.
    k = i
    # s = "198" s[0] = 1, s[1] = 9, s[2] = 8 
    for j in range(len(s)):
        k = k + int(s[j])
    if(k == n): #해를 찾는 순간 최솟값 저장 후 break
        ans = i
        break

print(ans)