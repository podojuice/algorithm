arr = [[],[2,3,4],[7,8,9],[12,14],[15],[],[],[10],[11],[],[],[],[13],[],[16,17],[],[],[]]


def tree(now, k):

    if arr[now]:
        if len(arr[now]) == 1:
            print('-----', end='')
            print('[0{}]'.format(arr[now][0]), end='')
        else:
            for i in range(len(arr[now])):
                if i == 0:
                    if arr[now][i] < 10:
                        print('--+--', end='')
                        print('[00{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k+1)
                    elif arr[now][i] < 100:
                        print('--+--', end='')
                        print('[0{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k + 1)
                    else:
                        print('--+--', end='')
                        print('[{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k + 1)
                elif i == len(arr[now])-1:
                    if arr[now][i] < 10:
                        print('L--', end='')
                        print('[00{}]'.format(arr[now][i]), end='')

                        tree(arr[now][i], k+1)
                    elif arr[now][i] < 100:
                        print('L--', end='')
                        print('[0{}]'.format(arr[now][i]), end='')

                        tree(arr[now][i], k + 1)
                    else:
                        print('L--', end='')
                        print('[{}]'.format(arr[now][i]), end='')

                        tree(arr[now][i], k + 1)
                else:
                    if arr[now][i] < 10:
                        print('+--', end='')
                        print('[00{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k+1)
                    elif arr[now][i] < 100:
                        print('+--', end='')
                        print('[0{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k + 1)
                    else:
                        print('+--', end='')
                        print('[{}]'.format(arr[now][i]), end='')
                        tree(arr[now][i], k + 1)

    print()
    if k == 1:
        jump = '       ' * k
        print(jump, end='')
    else:
        jump = '         ' * k
        print(jump, end='')


root = 1

now = root
print('[00{}]'.format(now), end='')

tree(now, 0)
