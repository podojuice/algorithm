# import sys
#
# sys.stdin = open('B1.txt')
#
# C, B = map(int, input().split())
#
# L = list(map(int, input().split()))
# black_jack = 0
# for i in range(1 << len(L)):
#     cnt = 0
#     for k in str(bin(i)):
#         if k == '1':
#             cnt += 1
#     if cnt == 3:
#         temp = 0
#         for j in range(len(L)):
#             if i & (1<<j):
#                 temp += L[j]
#                 if temp > B:
#                     break
#
#         if temp <= B and temp > black_jack:
#             black_jack = temp
#
# print(black_jack)

import sys

sys.stdin = open('B1.txt')

C, B = map(int, input().split())

L = list(map(int, input().split()))
black_jack = 0

for i in range(len(L)):
    for j in range(len(L)-i-1):
        for k in range(len(L)-i-j-2):
            temp = L[i] + L[i + j + 1] + L[i + j + k + 2]
            if temp <= B and temp > black_jack:
                black_jack = temp



print(black_jack)

