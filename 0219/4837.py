import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    n = len(arr)

    temp = []
    number = 0
    ans = 0
    a = N[0]

    for i in range((1 << a)-1, 1 << n):
        result = []
        number = 0
        for j in range(n):

            if i & (1 << j):
                result += [arr[j]]
                number += arr[j]

                # print(result, number, len(result), N[0], N[1])
        if len(result) == N[0] and number == N[1]:
            ans+=1
    print(f'#{test_case} {ans}')