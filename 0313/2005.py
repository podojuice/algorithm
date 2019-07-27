import sys

sys.stdin = open('2005.txt')

T = int(input())

memo = [[1], [1, 1]]


for test_case in range(1, T+1):
    N = int(input())
    for i in range(1, N+1):
        if len(memo) >= i:
            pass
        else:
            temp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    temp.append(1)
                else:
                    temp += [memo[i-2][j-1]+memo[i-2][j]]
            memo.append(temp)
            # print(memo)
    print('#{}'.format(test_case))
    for i in range(test_case):
        for j in memo[i]:
            print(j, end=' ')
        print()