ip = '0000000111100000011000000111100110000110000111100111100111111001100111'

cnt = 0

temp = []

for i in range(0, len(ip), 7):
    temp.append([int('0b'+ip[i:i+7], 2)])

print(temp)