import sys

sys.stdin = open('5185.txt', 'r')

T = int(input())

def make_bi(a):
    pass

for test_case in range(1, T+1):
    A, B = list(map(str, input().split()))
    temp = []
    for i in B:
        temp += [i]
    print(temp)