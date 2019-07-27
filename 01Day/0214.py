import sys
sys.stdin = open('1267.txt', 'r')

for test_case in range(10):
    T = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(len(data) - 4):
        if max(data[i:i + 5]) == data[i + 2]:
            tmp = data[i:i + 5]
            tmp.pop(2)
            next = max(tmp)
            count += data[i + 2] - next
    print (f'#{test_case + 1} {count}')
