import sys
sys.stdin = open('2383.txt')


def cal(fi, se):
    global MIN
    fi_num = X[st[0][0]][st[0][1]]
    se_num = X[st[1][0]][st[1][1]]
    for i in range(len(fi)):
        # fi에 저장된 좌표를 통해서 몇 분 뒤부터 계단을 내려가기 시작할 수 있는지 정보 저장.
        fi[i] = abs(st[0][0]-fi[i][0])+abs(st[0][1]-fi[i][1])+1

    for i in range(len(se)):
        # se에 저장된 좌표를 통해서 몇 분 뒤부터 계단을 내려가기 시작할 수 있는지 정보 저장.
        se[i] = abs(st[1][0]-se[i][0])+abs(st[1][1]-se[i][1])+1

    fi.sort()
    se.sort()
    fi_time = 0
    se_time = 0
    # print(fi, se)
    if fi:
        if len(fi) > 3:
            key = (len(fi)-1) % 3
            fi_time = fi[key]+fi_num
            for p in range(key+3, len(fi), 3):
                if fi[p] < fi_time:
                    fi_time += fi_num
                else:
                    fi_time = fi[p]+fi_num
        else:
            fi_time = fi[-1]+fi_num

    if se:
        if len(se) > 3:
            key = (len(se) - 1) % 3
            se_time = se[key] + se_num
            for p in range(key + 3, len(se), 3):
                if se[p] < se_time:
                    se_time += se_num
                else:
                    se_time = se[p] + se_num
        else:
            se_time = se[-1] + se_num
    # print(fi_time, se_time)
    result = max(fi_time, se_time)

    MIN = min(MIN, result)


def bi():
    for i in range(1 << len(pe)):
        x = []
        y = []
        for j in range(len(pe)):
            if i & 1 << j:
                x.append(pe[j])
            else:
                y.append(pe[j])
        # print(x, y)
        cal(x, y)


T = int(input())
for t in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    pe = []
    st = []

    for i in range(N):
        for j in range(N):
            if X[i][j] == 1:
                pe.append([i, j])
            elif X[i][j] > 1:
                st.append([i, j])
    MIN = 0xffffffffff
    bi()
    print('#{} {}'.format(t, MIN))
