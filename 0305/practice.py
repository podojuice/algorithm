import sys

sys.stdin = open('tree.txt', 'r')


def inorder(v):

    if v == 0: return
    # 여기서 뭔가 하면 전위순회
    print(v, end=' ')
    inorder(L[v])
    # 여기서 뭔가 하면 중위 순회
    # print(v, end=' ')
    inorder(R[v])
    # 여기서 뭔가 하면 후위 순회가 된다.
    # print(v, end=' ')

V, E = map(int, input().split()) # 노드수간선수

arr = list(map(int, input().split()))

L = [0]*(V+1)
R = [0]*(V+1)
P = [0]*(V+1)

for i in range(0, E*2, 2):
    u, v = arr[i], arr[i+1]
    if L[u] == 0: L[u] = v
    else: R[u] = v
    P[v] = u

# inorder(1)


# def treeHeight(v):
#     global max_num
#     global cnt
#     cnt += 1
#     if cnt == 3 and v: # 높이가 3인 친구들 출력
#         print(v)
#     if v == 0: # 트리의 높이 계산
#         if max_num < cnt-1:
#             max_num = cnt-1
#         return
#     # 여기서 뭔가 하면 전위순회
#     # print(v, end=' ')
#     treeHeight(L[v])
#     # 여기서 뭔가 하면 중위 순회
#     # print(v, end=' ')
#     treeHeight(R[v])
#     # 여기서 뭔가 하면 후위 순회가 된다.
#     # print(v, end=' ')

# max_num = 0
# cnt = 0
# treeHeight(1, 0)


# def treeSize(v):
#     global max_num
#     if v == 0:
#         return
#     # 여기서 뭔가 하면 전위순회
#     # print(v, end=' ')
#     order.append(v)
#     treeSize(L[v])
#     # 여기서 뭔가 하면 중위 순회
#     # print(v, end=' ')
#     treeSize(R[v])
#     # 여기서 뭔가 하면 후위 순회가 된다.
#     # print(v, end=' ')
#     if max_num < len(order):
#         max_num = len(order)
#
# order = []
# max_num = 0
# treeSize(5)
# print(max_num)



def makeorder(v):
    if v == 0: return
    # 여기서 뭔가 하면 전위순회
    order.append(v)
    makeorder(L[v])
    # 여기서 뭔가 하면 중위 순회
    # print(v, end=' ')
    makeorder(R[v])
    # 여기서 뭔가 하면 후위 순회가 된다.
    # print(v, end=' ')

order = []

makeorder(1)

def findsame(a, b):
    order_a= []
    order_b= []
    # print(order)
    for i in order:
        if i == a:
            break
        order_a += [i]

    for i in order:
        if i == b:
            break
        order_b += [i]
    print(order_a, order_b)
    result = []
    for i in order_a:
        if i in order_b:
            result += [i]
    return result


print(findsame(5, 6))
