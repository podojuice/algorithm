import sys
from copy import deepcopy

sys.stdin = open('5656.txt')

T = int(input())

# W중에 구슬을 떨굴 n을 지정해서 crash 함수로 넘겨주면, 1이면 그냥 없애고, 1보다 큰 숫자면 bomb 함수로 넘겨준다.


def crash(c):
    global H, W
    for i in range(H):
        if B[i][c] != 0:
            l = i
            break
    else:
        return
    if B[l][c] == 1:
        B[l][c] = 0
        return
    elif B[l][c]>1:
        bomb(l, c)
        # bomb 시켰으니 다시 중력에 의해 남은 찌끄레기들이 바닥으로 모여야한다. 그걸 만들어야 하는데..
        # 바닥부터 본다. 내가 0이라면, 내 위에를 봐서 0이 아닌 친구를 내 자리로 데려온다.
        for i in range(W):
            for j in range(H):
                if B[-1-j][i] == 0:
                    for k in range(1, H-j):
                        if B[-1-j-k][i] != 0:
                            B[-1-j][i] = B[-1-j-k][i]
                            B[-1 - j - k][i] = 0
                            break
    # 남은 벽돌의 수 리턴??

# bomb 함수에서는, 자기 숫자에 따라서 주변에 있는 숫자를 0을 만들어나간다. 그 와중에 1보다 큰 숫자를 만나면, 다시 bomb 함수에 집어 넣어 B 2차원 리스트에서 1을 지워나가는 식으로.


def bomb(l, c):
    global W, H
    key = B[l][c]
    B[l][c] = 0
    # route = [[1,0], [-1, 0], [0, 1], [0, -1]]
    for i in range(1, key):
        if l-i >= 0:
            if B[l-i][c] == 1:
                B[l - i][c] = 0
            elif B[l-i][c] > 1:
                bomb(l-i, c)
        if l+i <= H-1:
            if B[l+i][c] == 1:
                B[l + i][c] = 0
            elif B[l+i][c] > 1:
                bomb(l+i, c)
        if c-i >= 0:
            if B[l][c-i] == 1:
                B[l][c - i] = 0
            elif B[l][c - i] > 1:
                bomb(l, c - i)
        if c+i <= W-1:
            if B[l][c+i] == 1:
                B[l][c + i] = 0
            elif B[l][c + i] > 1:
                bomb(l, c + i)

def make_some(N, cnt, temp=[]):
    if cnt == N:
        temp2 = temp[:]
        result.append(temp2)
        return
    for i in range(W):
        temp2 = temp+[i]
        make_some(N, cnt+1, temp2)


N, W, H = map(int, input().split())
Z = []
for _ in range(H):
    Z.append(list(map(int, input().split())))

# 0번 col에 있는 애 한 번 없애보자.
# crash함수 끝.

# 지금 내 생각은, 그냥 3번 들어오면 10의 3승 해서 모든 경우 구해서 남아있는 숫자 저장하는 리스트 만들어서 거기서 min 구하기.

#재귀로 조합만들기. len(W) 안에 있는 숫자들 중 중복을 허용해 숫자를 N개 뽑아내야 한다.

result = []
min_num = 1000000000000000
make_some(N, 0)
for i in result:
    cnt = 0
    B = deepcopy(Z)
    for j in i:
        crash(j)

    for j in B:
        for k in j:
            if k != 0:
                cnt += 1
    if cnt < min_num:
        min_num = cnt



print(min_num)

