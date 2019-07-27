# import sys
#
# sys.stdin = open('practice.txt', 'r')
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     X =[]
#     for i in range(N):
#         X += [list(map(int, input().split()))]
#     cnt = 0
#     result = []
#
#     min_num = 0
#     for i in range(len(X)):
#         cnt += 1
#         temp = [0]
#         for j in range(len(X)-cnt):
#             temp += [X[i][j+cnt]+X[j+cnt][i]]
#
#         result += [temp]
#     key = []
#     cnt =0
#     for i in range(len(result)-1):
#         cnt += 1
#         for j in range(len(result[i])-1):
#             if i == i or i == j or j == j:
#
#     print(result)

arr = "ABCD"
N = len(arr)

for subset in range(1<<N):
    cntA = cntB = 0
    for i in range(N):
        if subset & (1 << i ): cntA += 1
        else: cntB += 1

    A, B = [], []
    if cntA == cntB:
        for i in range(N):
            if subset & (1 << i) : A.append(arr[i])
            else: B.append(arr[i])
        print(A,B)