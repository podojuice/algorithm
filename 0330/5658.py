import sys

sys.stdin = open('5658.txt')

T = int(input())
for t in range(1, 4):
    N, K = map(int, input().split())

    X = input()
    new_str = X

    po = []

    num = N//4
    print(num)
    for i in range(num):
        for j in range(0, N, num):
            if new_str[j:j+num] not in po:
                po.append(new_str[j:j+num])

        new_str = new_str[-1] + new_str[:-1]
    print(po)
    for i in range(len(po)):
        po[i] = int(po[i], 16)

    po = sorted(po)
    print(po)
    print('#{} {}'.format(t, po[-K]))
