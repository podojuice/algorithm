import sys

sys.stdin = open("song.txt","r")

arr = []
lengtha = int(input())
for i in range(lengtha):
    arr.append(list(map(int,input().split())))
for iy in range()