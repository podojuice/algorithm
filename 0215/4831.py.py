import sys
sys.stdin = open('sample_input2.txt', 'r')
T = int(input())
for test in range(1, T+1):
    N = list(map(int, input().split()))
    X = list(map(int, input().split()))
    if X[0] > N[0] or X[N[2] - 1] + N[0] < N[1]:
        print(f'#{test} 0')
    for i in range(len(X) - 1):
        if X[i + 1] - X[i] > N[0]:
            print(f'#{test} 0')
            break
    # 안될때 끝.
    else:
        X += [N[1]]

        # 될 때 시작
        temp = []
        temp += [X[0]]
        count = 0
        for i in range(len(X) - 1):
            temp += [X[i + 1] - X[i]]
        while len(temp) > 1:

            if sum(temp) <= N[0]:
                break

            a = 0
            for i in range(len(temp)):
                a += temp[i]
                if a == N[0]:
                    temp = temp[i + 1:]
                    count += 1
                    break
                if a > N[0]:
                    temp = temp[i:]
                    count += 1
                    break

        print(f'#{test} {count}')






