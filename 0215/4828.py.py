import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N = input()
    X = list(map(int, input().split()))
    max_num = X[0]
    min_num = X[0]
    for i in X:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i


    print(f'#{test} {max_num-min_num}')

