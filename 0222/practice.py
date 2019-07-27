# 스택 기본 클래스

# class Stack:
#     def __init__(self):
#         self.arr = []
#
#     def push(self, item):
#         self.arr.append(item)
#
#     def pop(self):
#         return self.arr.pop(-1)
#
#     def isEmpty(self):
#         return len(self.arr) == 0
#
# S = Stack()
#
# for i in range(5):
#     S.push((i, i))
#
# while not S.isEmpty():
#     x, y = S.pop()
#     print(x, y)


# # 괄호의 짝을 검사하는 프로그램
#
# test_1 = '()()((()))'
#
# test_2 = '((()((((()()((()())((()))))'
#
# test_3 = '[}'
#
# test_4 = '[{}([])({(()()(())){}})]'
#
#
# start = ['(', '{', '[']
# end = [')', '}', ']']

# def check(n):
#     stack = []
#     for i in n:
#         if i == '(':
#             stack += [')']
#         if i == ')':
#             if len(stack):
#                 stack.pop(-1)
#     if len(stack):
#         return False
#     else:
#         return True
#
# print(check(test_1), check(test_2))

# 여러가지 케이스의 경우.

# def check(n):
#     stack = []
#     for i in n:
#         for j in range(len(start)):
#             if i == start[j]:
#                 stack += [i]
#             elif i == end[j]:
#                 if stack:
#                     if stack[-1] == start[j]:
#                         stack.pop(-1)
#                     else:
#                         return False
#                 else:
#                     return False
#     if stack:
#         return False
#     else:
#         return True
#
# print(check(test_1), check(test_2), check(test_3), check(test_4))




# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# def fact(n):
#     return 1 if n == 1 else n * fact(n-1)
#
# print(fact(5))

cnt = 0
bit = [0]* 3
def printHello(i, n):
    global cnt
    if i == n:
        print(bit)
        cnt += 1
        return
    bit[i] = 1
    printHello(i+1, n)
    bit[i] = 0
    printHello(i+1, n)


printHello(0, 3)
print(cnt)

memo = [0] * 101

def fibo(n):
    if n < 2: return n
    if memo[n] != 0 :
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]


print(fibo(40))

memo = [0] * 101
memo[1] = 1
for i in range(2, 41):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[40])