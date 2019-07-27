K = 4
A = [0, 4, 1, 3, 1, 2, 4, 1]
B = [0] * len(A)
cnt = [0] * (K + 1)

for val in A:
    cnt[val] += 1
print(cnt)
for i in range(1, K + 1):
    cnt[i] += cnt[i - 1]
print(cnt)
for i in range(len(A) - 1, 0, -1):

    cnt[A[i]] -= 1
    B[cnt[A[i]]] = A[i]

print(cnt)
print(A)
print(B)
