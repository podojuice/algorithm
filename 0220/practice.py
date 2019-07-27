num = 12345
# 이걸 문자열로 바꿔보자.

A = []

while num !=0:
    A += [num % 10]
    num = num // 10

for i in range(len(A)//2):
    A[i], A[-1-i] = A[-1-i], A[i]


print(A)

