import sys

sys.stdin = open('4366.txt')

T = int(input())

for test_case in range(1, T+1):

    A = input()
    B = input()
    a = int(A, 2)
    b = int(B, 3)

    po_1 = []
    po_2 = []
    for i in range(1, len(A)+1):
        if A[-i] == '1':
            po_1.append(a - 2**(i-1))
        else:
            po_1.append(a + 2**(i-1))

    for i in range(1, len(B)+1):
        if B[-i] == '1':
            po_2.append(b - 3**(i-1))
            po_2.append(b + 3**(i-1))
        elif B[-i] == '2':
            po_2.append(b - 3 ** (i - 1))
            po_2.append(b - 3 ** (i - 1) * 2)
        elif B[-i] == '0':
            po_2.append(b + 3 ** (i - 1))
            po_2.append(b + 3 ** (i - 1) * 2)

    for i in po_1:
        if i in po_2:
            result = i
            break
    print(po_1, po_2)
    print('#{} {}'.format(test_case, result))
