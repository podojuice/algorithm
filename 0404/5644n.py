import sys

sys.stdin = open('5644.txt')

T = int(input())
for t in range(1, T+1):
    time, BC = map(int, input().split())

    zi = [[[] for _ in range(10)] for _ in range(10)]

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    BC_list = []
    for _ in range(BC):
        x, y, c, p = map(int, input().split())
        BC_list.append(p)
        for i in range(10):
            for j in range(10):
                if abs(x-1-i)+abs(y-1-j) <= c:
                    zi[j][i].append(_)

    a = [0, 0]
    b = [9, 9]

    a_sum = 0
    b_sum = 0

    if zi[a[0]][a[1]]:
        MAX = BC_list[zi[a[0]][a[1]][0]]
        for i in zi[a[0]][a[1]]:
            if BC_list[i] > MAX:
                MAX = BC_list[i]
        a_sum += MAX

    if zi[b[0]][b[1]]:
        MAX = BC_list[zi[b[0]][b[1]][0]]
        for i in zi[b[0]][b[1]]:
            if BC_list[i] > MAX:
                MAX = BC_list[i]
        b_sum += MAX

    route = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(time):
        a = [a[0]+route[A[i]][0], a[1]+route[A[i]][1]]
        b = [b[0]+route[B[i]][0], b[1]+route[B[i]][1]]

        temp_a = []
        temp_b = []
        if zi[a[0]][a[1]]:
            for j in zi[a[0]][a[1]]:
                temp_a.append([BC_list[j], j])

        if zi[b[0]][b[1]]:
            for j in zi[b[0]][b[1]]:
                temp_b.append([BC_list[j], j])
        temp_a.sort(reverse=True)
        temp_b.sort(reverse=True)
        if temp_a or temp_b:
            if not temp_a:
                b_sum += temp_b[0][0]
            elif not temp_b:
                a_sum += temp_a[0][0]
            else:
                if len(temp_a) >= 2:
                    if len(temp_b) == 1:
                        if temp_a[0] == temp_b[0]:
                            a_sum += temp_a[1][0]
                            b_sum += temp_b[0][0]
                        else:
                            a_sum += temp_a[0][0]
                            b_sum += temp_b[0][0]
                    else:
                        if temp_a[0] == temp_b[0]:
                            if temp_a[1][0] > temp_b[1][0]:
                                a_sum += temp_a[1][0]
                                b_sum += temp_b[0][0]
                            else:
                                a_sum += temp_a[0][0]
                                b_sum += temp_b[1][0]
                        else:
                            a_sum += temp_a[0][0]
                            b_sum += temp_b[0][0]
                else:
                    if len(temp_b) == 1:
                        if temp_a[0] == temp_b[0]:
                            a_sum += (temp_a[0][0])//2
                            b_sum += (temp_a[0][0])//2
                        else:
                            a_sum += temp_a[0][0]
                            b_sum += temp_b[0][0]
                    else:
                        if temp_a[0] == temp_b[0]:
                            a_sum += temp_a[0][0]
                            b_sum += temp_b[1][0]
                        else:
                            a_sum += temp_a[0][0]
                            b_sum += temp_b[0][0]

    print('#{} {}'.format(t, a_sum + b_sum))
