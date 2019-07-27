import sys

sys.stdin = open('4873.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = input()
    temp = []
    for i in N:
        temp += [i]
    while len(temp) > 1:
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                temp.pop(i+1)
                temp.pop(i)
                break
        else:
            break
    print(temp)