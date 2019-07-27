import sys

sys.stdin = open('workshop.txt', 'r')

for j in range(1, 11):

    N = int(input())
    L = [0]*(N+1)
    R = [0]*(N+1)
    P = [0]*(N+1)
    temp = []
    A = []


    for i in range(N):
        temp += [list(input().split())]

    for i in range(len(temp)):
        if len(temp[i]) == 4:
            L[int(temp[i][0])] = int(temp[i][2])
            R[int(temp[i][0])] = int(temp[i][3])
        elif len(temp[i]) == 3:
            L[i+1] =int(temp[i][2])

        A.append(temp[i][1])
    result = []
    print(L, R)
    def inorder(a):
        if a == 0: return
        inorder(L[a])
        result.append(A[a-1])
        inorder(R[a])

    # inorder(1)
    # print("#{} {}".format(j, ''.join(result)))

