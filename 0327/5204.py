import sys

sys.stdin = open('5204.txt')

# 찐 병합 정렬

# def mer(X):
#     global cnt
#     if len(X) == 1:
#         return X
#     else:
#         a, b = X[0:len(X) // 2], X[len(X) // 2:]
#         result = []
#         c = mer(a)
#         d = mer(b)
#         if c[-1] > d[-1]:
#             cnt += 1
#         while c and d:
#             if c[0] < d[0]:
#                 result.append(c.pop(0))
#             else:
#                 result.append(d.pop(0))
#         if c:
#             while c:
#                 result.append(c.pop(0))
#         if d:
#             while d:
#                 result.append(d.pop(0))
#
#         return result

# 짭 병합 정렬

def mer(X):
    global cnt
    if len(X) == 1:
        return X
    else:
        a, b = X[0:len(X) // 2], X[len(X) // 2:]
        c = mer(a)
        d = mer(b)
        if c > d:
            cnt += 1
            return c
        else:
            return d


T = int(input())
for t in range(1, T+1):
    N = int(input())

    X = list(map(int, input().split()))

    cnt = 0
    mer(X)
    k = sorted(X)
    print('#{} {} {}'.format(t, k[N//2], cnt))
