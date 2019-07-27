import sys

sys.stdin = open('5120.txt')

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

    def result(self, idx):
        for i in range(idx):
            print(mylist.printat(mylist.size-1-i), end=' ')

    def printat(self, idx):
        cur = self.head
        for i in range(idx):
            cur = cur.next
        return cur.data

    def findat(self, key):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.data > key:
                return idx
            cur = cur.next
            idx += 1
        else:
            return idx

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
    N, M, K = map(int, input().split())

    # 숫자 N개, M번째 칸에 K 번 추가

    X = list(map(int, input().split()))

    idx = 0
    mylist=List()

    for i in range(len(X)):
        mylist.insertlast(X[i])
    for _ in range(K):
        idx += M
        if idx > mylist.size:
            idx -= mylist.size
        if idx == mylist.size:
            mylist.insertAt(idx+1, mylist.printat((idx) % mylist.size)+mylist.printat(idx-1))
        else:
            mylist.insertAt(idx % mylist.size, mylist.printat((idx) % mylist.size) + mylist.printat((idx - 1) % mylist.size))

    if mylist.size >= 10:
        print('#{}'.format(test_case), end=' ')
        mylist.result(10)
        print()
    else:
        print('#{}'.format(test_case), end=' ')
        mylist.result(mylist.size)
        print()
