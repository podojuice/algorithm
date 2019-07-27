import sys


sys.stdin = open('workshopinput.txt', 'r')


for i in range(10):
    T = int(input())
    result = []
    for i in range(100):
        X = list(map(int, input().split()))
        result +=[X]
    max_num = 0
    for i in range(100):
        temp = 0
        for j in result[i]:
            temp += j
        if max_num < temp:
            max_num = temp
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += result[j][i]
        if max_num < temp:
            max_num = temp
    temp = 0
    for i in range(100):
        temp += result[i][i]
    if max_num < temp:
        max_num = temp
    temp = 0
    for i in range(100):
        temp += result[i][100-i-1]
    if max_num < temp:
        max_num = temp

    print(f'#{T} {max_num}')