import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    X = []
    result = []
    for i in range(10):
        result += [[0] * 10]
    for i in range(N):
        X += [list(map(int, input().split()))]

    for i in X:
        # print(i)
        a = i[0]-1
        for j in range(i[2]-i[0]+1):
            b = i[1]
            a += 1
            for k in range(i[3]-i[1]+1):
                # print(i[3], i[1], a, b)
                result[a][b] += i[4]
                # print(a,b,result)
                b+=1

    number=0
    for i in result:
        for j in range(10):
            if i[j]==3:
                number+=1
    print(f'#{test_case} {number}')