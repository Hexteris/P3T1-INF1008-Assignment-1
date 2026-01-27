class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = newNode

    #Worst case: O(n)
    def get(self, position):
        currNode = self.head
        for i in range(position-1):
            currNode = currNode.next
        return currNode.data

    #Worst case: O(n)
    def insert(self, position, value):
        newNode = Node(value)
        currNode = self.head
        for i in range(position - 2):
            currNode = currNode.next
        newNode.next = currNode.next
        currNode.next = newNode

    #Worst case: O(n)
    def delete(self, position):
        currNode = self.head
        for i in range(position-2):
            currNode = currNode.next
        currNode.next = currNode.next.next

    def printAll(self):
        if self.head != None:
            currNode = self.head
            while currNode.next != None:
                print(currNode.data)
                currNode = currNode.next
            print(currNode.data)
"""
testList = LinkedList()
testList.append("A")
testList.append("B")
testList.append("C")
testList.append("D")
testList.insert(3,"x")
testList.insert(3,"y")
testList.insert(5,"z")
testList.delete(3)
testList.printAll()
print()
print(testList.get(5))
"""


class ModifiedLinkedList:
    def __init__(self):
        self.head = None
        self.array = []

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currNode = self.head
            while currNode.next != None:
                currNode = currNode.next
            currNode.next = newNode
        self.array.append(newNode)

    #O(1)
    def get(self, position):
        if position-1 < 0 or position-1 > len(self.array):
            print("Position out of bounds")
        else:
            return self.array[position-1].data

    #O(1)
    def insert(self, position, value):
        newNode = Node(value)
        if position-1 < 0 or position-1 > len(self.array):
            print("Position out of bounds")
        elif position == 1:
            newNode.next = self.array[0]
            self.head= newNode
            self.array.insert(0, newNode)
        else:
            prevNode = self.array[position-2]
            newNode.next = prevNode.next
            prevNode.next = newNode
            self.array.insert(position-1, newNode)

    #O(1)
    def delete(self, position):
        if position-1 < 0 or position-1 > len(self.array):
            print("Position out of bounds")
        else:
            targetNode = self.array[position-2]
            targetNode.next = targetNode.next.next
            self.array.pop(position-1)

    def printAll(self):
        if self.head != None:
            currNode = self.head
            while currNode.next != None:
                print(currNode.data)
                currNode = currNode.next
            print(currNode.data)

testList = ModifiedLinkedList()
testList.append("A")
testList.append("B")
testList.append("C")
testList.append("D")
testList.insert(1,"x")
testList.insert(3,"y")
testList.delete(3)
testList.printAll()