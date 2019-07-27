import sys

sys.stdin = open('3143.txt')

T = int(input())

# for test_case in range(1, T+1):
#     A, B = map(str, input().split())
#     print('#{} {}'.format(test_case, len(A)-(len(B)-1)*A.count(B)))

for test_case in range(1, T+1):
    A, B = map(str, input().split())
    cnt = 0
    i = 0
    while i < len(A)-len(B)+1:
        for j in range(len(B)):
            if A[i] != B[j]:
                i = i - j
                break
            else:
                i += 1
        else:
            cnt += 1
            i -= 1
        i += 1
    print('#{} {}'.format(test_case, len(A)-(len(B)-1)*cnt) )