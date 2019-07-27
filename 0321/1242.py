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
    for i in range(1, 5):
        if result[-i] != '0':
            key = i
            break
    result = '0'*(key-1)+result[:len(result)-key+1]
    result = result[-56:]

    return result


def check(x):
    temp_code_list=['']*10
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
                if (i//7*key)%2:
                    even.append(j)
                else:
                    odd.append(j)
    result = 0
    if (sum(odd)*3 + sum(even))%10 == 0:
        result += sum(even) + sum(odd)
        return result
    else:
        return 0


def check_len(x, now):
    b = 0
    while 1:
        if now - 14 < 0:
            break
        if x[now - 14] == '0':
            break
        b += 1

    return b



for test_case in range(1, 4):
    N, M = map(int, input().split())
    temp = []
    result = 0
    for _ in range(N):
        a = input()
        k = 1
        while k < M-13:
            if a[-k] != '0':
                now = M-k
                # 여기서 코드가 14자리일때, 28자리일때, 그이상을 찾아서 계속 가야함. 한 줄에 여러 놈 나오는 거는 상관 없을듯하고, 14자리인지, 28자리인지를 알아보면 될듯.

                h = check_len(a, now)

                code = a[now - (13 + h*14):now + 1]
                # 또한 코드가 중복된 놈이 나올 때, 그 놈은 빼고 세야함.

                if code not in temp:
                    temp.append(code)
                    bi = make_code(code)
                    # print(bi)
                    result += check(bi)

                    k += len(code)
                else:
                    k += len(code)
            k += 1

    print(temp, result)

