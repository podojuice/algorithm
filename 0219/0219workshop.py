import sys

sys.stdin = open('workshopinput.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    X = list(map(int, input().split()))

    temp = []
    for i in range(len(X)//2):
        for j in range(len(X)//2):
            if X[2*i] == X[(2*j)+1]:
                break
        else:
            temp += [X[2*i], X[2*i+1]]

    for j in range(len(X)//2):
        for i in range(len(X)//2):
            if temp[-1] == X[2*i]:
                temp += [X[2*i], X[2*i+1]]

    result = ''
    for i in temp:
        result += ' '+ str(i)


    print(f'#{test_case}{result}')
