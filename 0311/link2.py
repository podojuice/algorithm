from link import List, Node


# 프린트리스트

# mylist = List()
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
#
# mylist.head = n1
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# mylist.size = 5
# mylist.printlist()


# 인서트라스트


# mylist = List()
# mylist.insertlast(1)
# mylist.insertlast(2)
# mylist.insertlast(3)
# mylist.insertlast(4)
# mylist.insertlast(5)
# mylist.printlist()


# 인서트 퍼스트
# mylist = List()
# mylist.insertfirst(1)
# mylist.insertfirst(2)
# mylist.insertfirst(3)
# mylist.printlist()
#
# mylist.insertfirst(4)
# mylist.insertfirst(5)
# mylist.printlist()

#딜리트 라스트

# mylist = List()
# mylist.insertfirst(1)
# mylist.insertfirst(2)
# mylist.insertfirst(3)
# mylist.insertfirst(4)
# mylist.insertfirst(5)
# mylist.printlist()
#
# mylist.deletelast()
# mylist.deletelast()
# mylist.printlist()
#
# mylist.deletelast()
# mylist.deletelast()
# mylist.deletelast()
# mylist.printlist()

#d인서트엣

mylist = List()
mylist.insertfirst(1)
mylist.insertfirst(2)
mylist.insertfirst(3)
mylist.insertfirst(4)
mylist.insertfirst(5)
mylist.printlist()

mylist.insertAt(2, 100)
mylist.insertAt(4, 200)
mylist.printlist()

mylist.insertAt(3, -1)
mylist.printlist()