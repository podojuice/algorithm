import sys

sys.stdin = open('4014.txt')

T = int(input())


for test_case in range(1, T+1):
    N, X = map(int, input().split())


    M = []
    cnt = 0

    for _ in range(N):
        M.append(list(map(int, input().split())))



    # 가로 체크
    used = [[False]*N for _ in range(N)]

    for i in range(N):
        possible = True
        for j in range(N-1):
            if M[i][j] != M[i][j+1]:
                if M[i][j] - M[i][j+1] == 1:
                    for k in range(1, X):
                        if j+1+k < N:
                            if M[i][j+1] != M[i][j+1+k]:
                                possible = False
                                break
                        else:
                            possible = False
                            break
                    else:
                        for k in range(X):
                            if used[i][j+1+k] == True:
                                possible = False
                                break
                            used[i][j+1+k] = True
                    if possible == False:
                        break

                elif M[i][j] - M[i][j+1] == -1:
                    for k in range(1, X):
                        if j-k >= 0 :
                            if M[i][j] != M[i][j-k]:
                                possible = False
                                break
                        else:
                            possible = False
                            break
                    else:
                        for k in range(X):
                            if used[i][j-k] == True:
                                possible = False
                                break
                            used[i][j-k] = True
                    if possible == False:
                        break

                else:
                    possible = False
                    break

        else:
            cnt += 1



    # 세로 체크
    used = [[False] * N for _ in range(N)]

    for j in range(N):
        possible = True
        for i in range(N - 1):
            if M[i][j] != M[i+1][j]:
                if M[i][j] - M[i+1][j] == 1:
                    for k in range(1, X):
                        if i + 1 + k < N:
                            if M[i+1][j] != M[i + 1 + k][j]:
                                possible = False
                                break
                        else:
                            possible = False
                            break
                    else:
                        for k in range(X):
                            if used[i+1+k][j] == True:
                                possible = False
                                break
                            used[i+1+k][j] = True
                    if possible == False:
                        break

                elif M[i][j] - M[i+1][j] == -1:
                    for k in range(1, X):
                        if i - k >= 0:
                            if M[i][j] != M[i-k][j]:
                                possible = False
                                break
                        else:
                            possible = False
                            break
                    else:
                        for k in range(X):
                            if used[i-k][j] == True:
                                possible = False
                                break
                            used[i-k][j] = True
                    if possible == False:
                        break

                else:
                    possible = False
                    break

        else:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))