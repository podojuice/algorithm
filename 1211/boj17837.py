N , K = map(int, input().split())

zido = []

turn = 1

for i in range(N):
    zido.append(list(map(int , input().split())))
# 1 빨강 2 파랑 0 흰

mal = [[[] for _ in range(N)] for __ in range(N)]

knight =[]

# 1부터 오왼위아
for i in range(K):
    x, y, v = map(int, input().split())
    knight.append([x-1, y-1, v])
    mal[x-1][y-1].append(i)

print(zido, mal, knight)


