import sys

sys.stdin = open('B1244.txt')

T = int(input())

switch = list(map(int, input().split()))

N = int(input())

S = []

for i in range(N):
    S.append(list(map(int, input().split())))

for i in range(len(S)):
    if S[i][0] == 1:
        for j in range(len(switch)):
            if (j+1)%S[i][1] == 0:
                switch[j] = 0 if switch[j] == 1 else 1
    else:
        mid = S[i][1] -1
        cnt = 0
        while 0 <= mid-cnt and mid + cnt < len(switch):
            if switch[mid-cnt] == switch[mid+cnt]:
                if switch[mid-cnt] == 0:
                    switch[mid-cnt] = switch[mid+cnt] = 1
                else:
                    switch[mid - cnt] = switch[mid + cnt] = 0
                cnt += 1
            else:
                break
for i in range((T//20)+1):
    print(' '.join(map(str, switch[:21])))
    switch = switch[21:]
