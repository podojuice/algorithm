import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N = int(input())
    X = list(map(int, input()))

    result = [0]*10
    for i in X:
        result[i] += 1
    max = result[9]
    a = 9
    for i in range(len(result)-1):
        if max < result[9-i-1]:
            max = result[9-i-1]
            a = 9-i-1

    print(f'#{test} {a} {max}')