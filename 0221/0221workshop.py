import sys
sys.stdin = open('workshop.txt', 'r')


def check_pal(st):
    result = 0
    for i in range(len(st)//2):
        if st[i] != st[-1-i]:
            break
    else:
        result = len(st)
    return result


for test_case in range(1, 11):
    T = int(input())
    X = []
    max_num = 1
    for i in range(100):
        X += [input()]
    for k in range(len(X)):
        for i in range(len(X[k])):
            if len(X[k])-i> max_num:
                for j in range(len(X[k])-i):
                    # if len(X[k][i:i+j+1])>=max_num:
                    if check_pal(X[k][i:i+j+1])>=max_num:
                        max_num = check_pal(X[k][i:i+j+1])


    for k in range(len(X[0])):
        for i in range(len(X)):
            temp = []
            if len(X)-i>max_num:
                for j in range(len(X)-i):
                    temp += X[i+j][k]
                    # if len(temp)>=max_num:
                    if check_pal(temp) >= max_num:
                        max_num = check_pal(temp)


    print(f'#{test_case} {max_num}')