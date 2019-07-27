import sys

sys.stdin = open('1767.txt')


def DFS(n, k, num, line):
    global cell_num, result
    if n == k:
        if num > cell_num:
            cell_num = num
            result = line
        elif num == cell_num:
            if result > line:
                result = line
                print(used)
        return

    # 0 == x 1 == 동 2 == 서 3 == 남 4 == 북
    for i in range(5):
        if i == 0:
            DFS(n, k+1, num, line)
        elif i == 1:
            for p in range(cell[k][1]+1, N):
                if used[cell[k][0]][p]:
                    break
            else:
                temp = 0
                for p in range(cell[k][1] + 1, N):
                    used[cell[k][0]][p] = True
                    temp += 1
                DFS(n, k+1, num+1, line+temp)
                for p in range(cell[k][1] + 1, N):
                    used[cell[k][0]][p] = False

        elif i == 2:
            for p in range(cell[k][1]):
                if used[cell[k][0]][p]:
                    break
            else:
                temp = 0
                for p in range(cell[k][1]):
                    used[cell[k][0]][p] = True
                    temp += 1
                DFS(n, k+1, num+1, line+temp)
                for p in range(cell[k][1]):
                    used[cell[k][0]][p] = False

        elif i == 3:
            for p in range(cell[k][0]+1, N):
                if used[p][cell[k][1]]:
                    break
            else:
                temp = 0
                for p in range(cell[k][0]+1, N):
                    used[p][cell[k][1]] = True
                    temp += 1
                DFS(n, k+1, num+1, line+temp)
                for p in range(cell[k][0]+1, N):
                    used[p][cell[k][1]] = False

        elif i == 4:
            for p in range(cell[k][0]):
                if used[p][cell[k][1]]:
                    break
            else:
                temp = 0
                for p in range(cell[k][0]):
                    used[p][cell[k][1]] = True
                    temp += 1
                DFS(n, k+1, num+1, line+temp)
                for p in range(cell[k][0]):
                    used[p][cell[k][1]] = False


T = int(input())


for t in range(1, T+1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))

    # print(X)

    cell = []

    used = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if X[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    pass
                else:
                    cell.append([i, j])
                used[i][j] = True

    used_cell = [False]*len(cell)
    print(cell)
    cell_num = 0
    result = 0xffffffffff

    DFS(len(cell), 0, 0, 0)
    print(cell_num)
    print('#{} {}'.format(t, result))
