# 1은 흑, 2는 백

# for i in X:
#     a, b = i[0] - 1, i[1] - 1
#     if i[2] == 1:
#         B[a][b] = 'B'
#     else:
#         B[a][b] = 'W'
#     #새로 들어온놈 가로세로 리스트 생성
#     lr = B[a]
#     lc = []
#     for j in range(len(B)):
#         lc += [B[j][b]]
#     lr[b]
#
#
#     #새로 들어온놈 대각선 리스트 생성
#     lu = []
#     ld = []
#     x, y = a, b
#     while x > 0 and y > 0:
#         x -= 1
#         y -= 1
#     while x < N and y < N:
#         ld += [B[x][y]]
#         x += 1
#         y += 1
#     x, y = a, b
#     while x < N-1 and y > 0:
#         x += 1
#         y -= 1
#     while x >= 0 and y < N:
#         lu += [B[x][y]]
#         x -= 1
#         y += 1