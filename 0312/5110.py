import sys

sys.stdin = open('5110.txt')


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
        for i in range(10):
            result.append(cur.data)
            cur = cur.next
        # return cur.data

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
            for i in val:
                self.insertfirst(i)
        elif idx >= self.size:
            for i in val:
                self.insertlast(i)
        else:
            prev, cur = None, self.head
            for i in range(idx):
                prev = cur
                cur = cur.next
            if prev is None:
                for i in val:
                    self.insertfirst(i)
            else:
                for i in range(len(val)):
                    node = Node(val[-1-i])
                    node.next = prev.next
                    prev.next = node
                    self.size += 1




T = int(input())



for test_case in range(1, T+1):
    N, M = map(int, input().split())
    mylist = List()
    X = list(map(int, input().split()))

    for i in X:
        mylist.insertlast(i)

    # mylist.printlist()

    for i in range(M-1):
        X = list(map(int, input().split()))
        idx = mylist.findat(X[0])
        mylist.insertAt(idx, X)


    #이제 역순으로 10개 출력하면 된다.

    result = []
    mylist.printat(mylist.size-10)

    result = ' '.join(list(map(str, list(reversed(result)))))

    print('#{} {}'.format(test_case, result))
