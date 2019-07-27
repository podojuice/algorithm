import sys

sys.stdin = open('temp.txt')

soo = []
man = []
visit = []
for i in range(5):
    soo.append(list(map(int, input().split())))
    visit += [[False]*5]
for i in range(5):
    man += list(map(int, input().split()))
cnt = 0
bingo = 0
for i in range(len(man)):
    for j in range(5):
        for k in range(5):
            if man[i] == soo[j][k]:
                visit[j][k] = True
                cnt += 1
                print(visit)
                for p in range(5):#가로 확인
                    if not visit[j][p]: break
                else:
                    bingo += 1
                    if bingo == 3:
                        result = cnt

                for p in range(5):#세로 확인
                    if not visit[p][k]: break
                else:
                    bingo += 1
                    if bingo == 3:
                        result = cnt

                if j-2 == k-2:
                    for p in range(5):#우하향 대각 확인
                        if not visit[p][p]: break
                    else:
                        bingo += 1
                        if bingo == 3:
                            result = cnt

                if j-2 == -(k-2):#우상향 대각 확인
                    for p in range(5):
                        if not visit[p][-1-p]: break
                    else:
                        bingo += 1
                        if bingo == 3:
                            result = cnt

    if bingo >= 3:
        break

print(result)