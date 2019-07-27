import sys

sys.stdin = open('5122.txt')


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
            print('빈 리스트입니다.')
            return
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

    def deletelast(self):
        if self.head is None:
            print('빈 리스트')
        else:
            prev, cur = None, self.head
            while cur.next is not None:
                prev = cur
                cur = cur.next
            if prev is None:
                self.head = self.tail = None
                del cur
            else:
                prev.next = None
                self.tail = prev
                del cur

    def deletefirst(self):
        if self.head is None:
            print('빈 리스트')

        else:
            cur = self.head
            if cur.next is None:
                self.head = self.tail = None
            else:
                self.head = cur.next
            del cur
            self.size -= 1

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

    def deleteAt(self, idx):
        prev, cur = None, self.head
        for i in range(idx):
            prev = cur
            cur = cur.next
        if prev is None:
            self.deletefirst()
        else:
            prev.next = cur.next
            mylist.size -= 1
            del cur

    def change(self, idx, val):
        cur = self.head
        for i in range(idx):
            cur = cur.next
        cur.data = val


T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    S = list(map(int, input().split()))
    mylist = List()
    for i in S:
        mylist.insertlast(i)
    for _ in range(M):
        X = list(input().split())

        if X[0] == 'I':
            mylist.insertAt(int(X[1]), int(X[2]))

        elif X[0] == 'D':
            mylist.deleteAt(int(X[1]))

        elif X[0] == 'C':
            mylist.change(int(X[1]), int(X[2]))


    # mylist.printlist()
    if L >= mylist.size:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}'.format(test_case, mylist.printat(L)))

# print(mylist.printat(4))