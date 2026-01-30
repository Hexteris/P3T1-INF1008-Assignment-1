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
        if position-1 < 0 or position > len(self.array):
            print("Position out of bounds")
        elif position == 0:
            self.head == self.head.next
            self.array.pop(position)
        else:
            targetNode = self.array[position-1]
            targetNode.next = targetNode.next.next
            self.array.pop(position)

    def printAll(self):
            currNode = self.head
            while currNode:
                print(currNode.data, end=" -> " if currNode.next else "")
                currNode = currNode.next
            print()

if __name__ == "__main__":
    def testcase1():
        print("=== Test Case 1: GET ===")
        testList = ModifiedLinkedList()
        testList.append("A")
        testList.append("B")
        testList.append("C")
        testList.append("D")
        print("List contents:", end="")
        testList.printAll()

        # Test getting valid positions
        print(f"Get position 1: {testList.get(1)}") 
        print(f"Get position 3: {testList.get(3)}")  
        print(f"Get position 4: {testList.get(4)}")  
        
        # Test getting invalid positions
        print(f"Get position 0: {testList.get(0)}")  
        print(f"Get position 10: {testList.get(10)}") 

    def testcase2():
        print("=== Test Case 2: INSERT ===")
        testList = ModifiedLinkedList()
        testList.append("A")
        testList.append("B")
        testList.append("C")
        testList.append("D")
        print("List contents:", end="")
        testList.printAll()

        #Insert at beginning
        testList.insert(1, "X")
        print("Insert 'X' at position 1:")
        testList.printAll()
        
        # Insert in middle
        testList.insert(3, "Y")
        print("Insert 'Y' at position 3:")
        testList.printAll()
        
        # Insert at end
        testList.insert(6, "Z")
        print("Insert 'Z' at position 6:")
        testList.printAll()

    def testcase3():
        print("=== Test Case 3: DELETE ===")
        testList = ModifiedLinkedList()
        testList.append("A")
        testList.append("B")
        testList.append("C")
        testList.append("D")
        testList.append("E")
        print("List contents:", end="")
        testList.printAll()

        testList.delete(1)
        print("Delete position 1:")
        testList.printAll()

        testList.delete(3)
        print("Delete position 3:")
        testList.printAll()
        
testcase1()
testcase2()
testcase3()