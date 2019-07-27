import sys

sys.stdin = open('5644.txt')

T = int(input())

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
                if len(zi[j][i]) == 2:
                    for k in range(len(zi[j][i])):
                        if k < p:
                            zi[j][i].pop(k)
                            zi[j][i].append(_)
                            break
                else:
                    zi[j][i].append(_)

a = [0, 0]

b = [9, 9]

# 0 이동 x 1 북 2 동 3 남 4 서

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
    used = [False]*BC

    # a와 b의 새로운 좌표가 나왔다. 자신의 자리를 보고, 지금 충전이 가능한 충전소 번호를 임시 리스트에 저장.
    temp_a = []
    temp_b = []
    if zi[a[0]][a[1]]:
        for j in zi[a[0]][a[1]]:
            temp_a.append(j)

    if zi[b[0]][b[1]]:
        for j in zi[b[0]][b[1]]:
            temp_b.append(j)

    if temp_a or temp_b:
        if not temp_a and len(temp_b) == 1:
            b_sum += BC_list[temp_b[0]]
        elif not temp_b and len(temp_a) == 1:
            a_sum += BC_list[temp_a[0]]
        elif len(temp_a) == 1 and len(temp_b) == 1:
            if temp_a[0] == temp_b[0]:
                a_sum += (BC_list[temp_a[0]])//2
                b_sum += (BC_list[temp_a[0]])//2
            else:
                a_sum += (BC_list[temp_a[0]])
                b_sum += (BC_list[temp_b[0]])

        # 랭스 1, 2 그리고 2, 1 그리고 2, 0 그리고 0, 2 그리고 2, 2까지  못해먹ㄱㅆ다





