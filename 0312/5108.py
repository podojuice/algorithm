import sys

sys.stdin = open('5108.txt')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:
            print('빈 리스트')
        print(self.size, '[ ', end='')
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def printat(self, idx):
        cur = self.head
        for i in range(idx):
            cur = cur.next
        return cur.data

    def insertlast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insertAt(self, idx, val):
        if self.head is None:
            self.insertfirst(val)
        elif idx >= self.size:
            self.insertlast(val)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                self.insertfirst(val)
            else:
                node = Node(val)
                node.next = prev.next
                prev.next = node
                self.size += 1

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    X = list(map(int, input().split()))
    mylist = List()
    for i in X:
        mylist.insertlast(i)

    for i in range(M):
        x, y = map(int, input().split())
        mylist.insertAt(x, y)
    print('#{} {}'.format(test_case, mylist.printat(L)))