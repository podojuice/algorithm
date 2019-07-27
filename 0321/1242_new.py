import sys

sys.stdin = open('1242.txt')

T = int(input())



code_list = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
]


def make_code(x):
    result = ''
    for i in x:
        temp = str(bin(int(i, 16)))[2:]
        if len(temp) == 1:
            temp = '000' + temp
        elif len(temp) == 2:
            temp = '00' + temp
        elif len(temp) == 3:
            temp = '0' + temp
        result += temp

    result = result.rstrip('0')
    result = '0'*50 + result

    return result


def check(x):
    temp_code_list = ['']*10

    key = len(x)//56

    for i in range(len(code_list)):
        for j in code_list[i]:
            temp_code_list[i] += j*key

    even = []
    odd = []
    for i in range(0, len(x), 7*key):
        now = x[i:i+7*key]

        for j in range(len(temp_code_list)):
            if temp_code_list[j] == now:
                if (i//(7*key))%2:
                    even.append(j)
                else:
                    odd.append(j)

    if len(even) != 4 or len(odd) != 4:
        return -1
    result = 0
    if (sum(odd)*3 + sum(even)) % 10 == 0:
        result += sum(even) + sum(odd)
        return result
    else:
        return result




for test_case in range(1, 21):
    N, M = map(int, input().split())
    help_me = []
    result = 0
    for _ in range(N):
        a = input()
        a = a.rstrip('0')
        if a:
            b = make_code(a)
            while b:
                c = 1
                while 1:
                    temp = b[-(56*c):]
                    t = check(temp)
                    if t != -1:
                        if temp not in help_me:
                            help_me.append(temp)
                            result += t
                        break
                    else:
                        if c > 10:
                            break
                        c += 1

                b = b[:-56*c]

                b = b.rstrip('0')


    print(test_case, result)


# help_me = []
# b = make_code('F0FF000FF0F0FF000F0F000FF0F0FFFF000F0FF0F000FF0FF000F')
# c = 1
# result = 0
# while b:
#     while 1:
#         temp = b[-(56*c):]
#         t.py = check(temp)
#         print(temp)
#         if t.py != -1:
#             if temp not in help_me:
#                 help_me.append(temp)
#                 result += t.py
#             break
#         else:
#             if c > 10:
#                 break
#             c += 1
#
#     b = b[:-56*c]
#
#     b = b.rstrip('0')
#
# print(result)