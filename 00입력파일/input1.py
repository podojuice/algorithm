import sys

sys.stdin = open('input2.txt', 'r')

T=int(input())
for text_case in range(T):
        N = int(input())
        arr =[]
        for i in range(N):
            arr.append(list(map(int, input().split())))
        
        print(N)
        print(arr)


