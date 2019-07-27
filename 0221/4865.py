import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = input()
    X = input()
    result = [0]*len(N)
    for i in range(len(N)):
        for j in range(len(X)):
            if N[i] == X[j]:
                result[i] += 1
    max_num = result[0]
    for i in result:
        if i >= max_num:
            max_num = i
    print(f'#{test_case} {max_num}')