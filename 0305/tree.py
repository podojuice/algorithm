import sys

sys.stdin = open('tree.txt', 'r')

def inorder(v):
    if v == 0: return
    # 여기서 뭔가 하면 전위순회
    # print(v, end=' ')
    inorder(L[v])
    # 여기서 뭔가 하면 중위 순회
    # print(v, end=' ')
    order.append(v)
    inorder(R[v])
    # 여기서 뭔가 하면 후위 순회가 된다.
    print(v, end=' ')

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
order = []
inorder(1)

print(order)
print(L, R, P)