import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())

for text_case in range(1, T+1):
    N = input()
    X = input()
    i = 0
    result = 0
    while i < len(X):
        j = 0
        while j < len(N):
            if X[i] != N[j]:
                break
            j += 1
            i += 1
        if j == len(N):
            result = 1
        i = i + j + 1
    print(f'#{text_case} {result}')



