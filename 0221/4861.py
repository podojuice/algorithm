import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    X = []
    for i in range(N[0]):
        X += [input()]

    for i in range(N[0]):
        for j in range(N[0]-N[1]+1):
            for k in range(N[1]//2):
                if X[i][j+k] != X[i][N[1]+j-1-k]:
                    break
            else:
                result = X[i][j:j+N[1]]
                break
            for k in range(N[1]//2):
                if X[j+k][i] != X[N[1]+j-1-k][i]:
                    break
            else:
                result = ''
                for x in range(N[1]):
                    result += X[j + x][i]
                break
    print(result)



