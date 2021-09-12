N=int(input())
for i in range(1,N+1):
    arr=input().split()
    arr.reverse()
    print("Case #{0}:".format(i), ' '.join(arr))
