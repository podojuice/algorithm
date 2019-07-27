import sys

sys.stdin = open('1267.txt', 'r')



def max(a):
    num = a[0]
    idx = 0
    for i in range(len(a)):
        if a[i] > num:
            num = a[i]
            idx = i
    return [num, idx]
def min(a):
    num = a[0]
    idx = 0
    for i in range(len(a)):
        if a[i] < num:
            num = a[i]
            idx = i
    return [num, idx]


for i in range(10):
    T = int(input())
    N = list(map(int, input().split()))
    for j in range(T):
        N[max(N)[1]] -=1
        N[min(N)[1]] +=1
    print(f'#{i} {max(N)[0] - min(N)[0]}')


