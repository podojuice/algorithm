import sys

sys.stdin = open('5178.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    bin = [0]* (N+1)
    for i in range(M):
        u, v = map(int, input().split())
        bin[u] = v

    while not bin[1]:
        for i in range(1, len(bin)-1):
            if not bin[i]:
                if (2*i)+1 < len(bin) and bin[2*i] and bin[(2*i)+1]:
                    bin[i] = bin[2*i] + bin[(2*i)+1]
                else:
                    bin[i] = bin[2*i]

    print('#{} {}'.format(test_case, bin[L]))
