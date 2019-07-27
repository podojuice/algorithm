# 2진 선택. 부분집합 구하기.

bits =[0]*3
def subset(k, n):
    if k == n: # 모든 선택이 끝났다.
        print(bits)
    else: # 선택해야될 것이 남았다
        #선택지의 수만큼, 자식 노드의 수만큼
        # for i in range(2):
        #     bits[k] = i
        #     subset(k+1, n)
        bits[k] = 0
        subset(k + 1, n)
        bits[k] = 1
        subset(k + 1, n)

subset(0, 3) # 0은 root를 나타냄. 시작 상태. 3은 단말 노드의 높이를 나타냄.


# 순열
# 아까 이진 선택처럼 하면 중복순열이 된다. 3개의 자리, 3개의 인자가 있으면 3의 3제곱, 27개가 나오는데 이거 아니다. 중복된거 빼야한다.

arr = 'ABC'
N = len(arr)
for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if i == k or j == k: continue
            print(arr[i], arr[j], arr[k])

# 이걸 재귀로 만들어보자.

order = [0] * N

# def perm(k, n):
#     if k == n:
#         # order[] 저장된 순서를 확인
#         print(order)
#         return
#     visit = [False]*N
#     for i in range(k):
#         visit[order[i]] = True
#     for i in range(n):
#         if visit[i]: continue
#         order[k] = i
#         perm(k+1, n)
#
#
# perm(0, N) # N은 순열을 만드는 요소의 수. 단말 노트의 높이


def perm_1(k, n, visit):
    if k == n:
        # order[] 저장된 순서를 확인
        print(order)
        return

    for i in range(n):
        if visit & (1 << i): continue
        order[k] = i
        perm_1(k+1, n, visit | (1 << i))

perm_1(0, N, 0)