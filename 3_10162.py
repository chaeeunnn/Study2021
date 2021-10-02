import sys

T = int(sys.stdin.readline())

#버튼 누른 횟수
A_cnt = 0
B_cnt = 0
C_cnt = 0


if T%10 : #정확히 T초가 될 수 없는 경우
    print(-1)
    sys.exit() #프로그램 종료
elif T >= 300 :
    A_cnt += T//300
    B_cnt += (T%300)//60
    C_cnt += ((T%300)%60)//10
elif 60<=T<300 :
    B_cnt += T//60
    C_cnt += (T%60)//10
elif T<60:
    C_cnt = T//10

print(A_cnt, B_cnt, C_cnt)

