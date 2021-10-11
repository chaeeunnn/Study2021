import sys

K = int(sys.stdin.readline())
A_cnt=1
B_cnt=0
for i in range(K):
    click_A=A_cnt
    click_B=B_cnt

    A_cnt=click_B # A -> B
    B_cnt+=click_A # B -> BA

print(A_cnt, B_cnt)


