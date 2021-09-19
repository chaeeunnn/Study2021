n=int(input())
s=input()

# ord : char to int
ans = 0
for i in range(n):
    k = ord(s[i]) - ord('a') + 1 
    ans += k * 31 ** i # ** : 제곱

print(ans % 1234567891)