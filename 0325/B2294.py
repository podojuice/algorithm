import sys

sys.stdin = open('B2294.txt')

N, K = map(int, input().split())

coin_list = []

for _ in range(N):
    coin_list.append(int(input()))


D = [100001]*(K+1)
D[0] = 0

Q = [0]

for coin in coin_list:
    for j in range(coin, len(D)):
        if D[j] > D[j-coin]:
            D[j] = D[j-coin]+1


if D[K] > 100000:
    print(-1)
else:
    print(D[K])

