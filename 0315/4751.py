import sys

sys.stdin = open('4751.txt')

T = int(input())

dia_1 = [['..#..'], ['.#.#.'], ['#.{}.#'], ['.#.#.'], ['..#..']]
dia_2 = [['.#..'], ['#.#.'], ['.{}.#'], ['#.#.'], ['.#..']]
for test_case in range(1, T+1):
    X = input()
    result = [[], [], [], [], []]
    for i in range(len(X)):
        if i == 0 :
            key = dia_1
        else:
            key = dia_2
        for j in range(len(result)):
            if j == 2:
                result[j] += key[j][0].format(X[i])
            else:
                result[j] += key[j]
    for i in result:
        print(''.join(i))

