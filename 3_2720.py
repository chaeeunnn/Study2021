T = int(input())

Q, D, N, P = 25, 10, 5, 1

for n in range(0,T):
    Q_cnt, D_cnt, N_cnt, P_cnt = 0, 0, 0, 0
    C = int(input())
    if C >= Q :
        Q_cnt += C//Q
        D_cnt += (C%Q)//D
        N_cnt += ((C%Q)%D)//N
        P_cnt += (((C%Q)%D)%N)//P
    elif D <= C < Q :
        D_cnt += C//D
        N_cnt += (C%D)//N
        P_cnt += ((C%D)%N)//P
    elif N <= C < D :
        N_cnt += C//N
        P_cnt += (C%N)//P
    else :
        P_cnt += C//P
    print(Q_cnt, D_cnt, N_cnt, P_cnt)
        