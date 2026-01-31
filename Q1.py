import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #for testing 
    def append(self, value):
            newNode = Node(value)
            if self.head is None:
                self.head = self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode

    #Worst case: O(n)
    def get(self, position):
        currNode = self.head
        for i in range(position):
            currNode = currNode.next
        return currNode.data

    #Worst case: O(n)
    def insert(self, position, value):
        newNode = Node(value)
        start_time = time.process_time()
        currNode = self.head
        for i in range(position):
            currNode = currNode.next
        newNode.next = currNode.next
        currNode.next = newNode
        end_time = time.process_time()
        time_taken = end_time-start_time
        return time_taken

    #Worst case: O(n)
    def delete(self, position):
        currNode = self.head
        for i in range(position):
            currNode = currNode.next
        currNode.next = currNode.next.next

    def printAll(self):
        if self.head != None:
            currNode = self.head
            while currNode.next != None:
                print(currNode.data)
                currNode = currNode.next
            print(currNode.data)


class ModifiedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.array = []

    #for testing
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.array.append(newNode)









    #O(1)
    def get(self, position):
        if position < 0 or position > len(self.array):
            print("Position out of bounds")
        else:
            return self.array[position].data


    def insert(self, position, value):
        #time taken for node to be added to linked list
        initial_time_taken = 0 
        #total time taken for node to be added and array to be updated
        actual_time_taken = 0 
        #Create new node
        newNode = Node(value)

        #starts timer after node is created
        start_time = time.process_time() 

        #Index out of bounds
        if position < 0 or position > len(self.array):
            print("Position out of bounds")

        #Insert to front of list
        elif position == 0:
            
            #new node -> current head
            newNode.next = self.array[0]
            #update head 
            self.head= newNode

            #adds new node into auxiliary array
            self.array.insert(0, newNode)

        else:
            #jump to prev node in O(1)
            prevNode = self.array[position-1]
            #new node -> next node
            newNode.next = prevNode.next
            #prev node -> new node -> next node
            prevNode.next = newNode

            #Calculate time taken for node to be added to linked list
            end_time = time.process_time()
            initial_time_taken = end_time-start_time


            #adds new node into auxiliary array
            self.array.insert(position, newNode)

        #Calculate time taken for node to be added to linked list AND array
        end_time = time.process_time()
        actual_time_taken = end_time-start_time

        return initial_time_taken, actual_time_taken


    #O(1)
    def delete(self, position):
        if position < 0 or position > len(self.array):
            print("Position out of bounds")
        elif position == 0:
            self.head = self.head.next
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
        print(f"Get index 0: {testList.get(0)}") 
        print(f"Get index 2: {testList.get(2)}")  
        print(f"Get index 3: {testList.get(3)}")  
        
        # Test getting invalid positions
        print(f"Get index -1: {testList.get(-1)}")  
        print(f"Get index 10: {testList.get(10)}") 

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
        testList.insert(0, "X")
        print("Insert 'X' at index 0:")
        testList.printAll()
        
        # Insert in middle
        testList.insert(2, "Y")
        print("Insert 'Y' at index 2:")
        testList.printAll()
        
        # Insert at end
        testList.insert(5, "Z")
        print("Insert 'Z' at index 5:")
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

        testList.delete(0)
        print("Delete index 0:")
        testList.printAll()

        testList.delete(2)
        print("Delete index 2:")
        testList.printAll()

    def testcase4():
        print("=== Test Case 4 ===")
        print("Testing with 100000 records")   
        noOfTestCase = 1000000
        oldList = LinkedList()
        modifiedList = ModifiedLinkedList()

        print("generating records...")
        for i in range(noOfTestCase):
            oldList.append(Node(i))
            modifiedList.append(Node(i))

        print("calculating insert time for regular linked list...")
        old_timetaken = oldList.insert(int(noOfTestCase * 0.8), "x")
        print("calculating insert time for hybrid linked list...")
        initial_timetaken, actual_timetaken = modifiedList.insert(int(noOfTestCase * 0.8), "x")

        print("\n" + "="*70)
        print("                    PERFORMANCE COMPARISON RESULTS")
        print("="*70)
        print(f"{'Operation':<25} {'Time (s)':<12} {'Speedup vs Regular':<18}")
        print("-"*70)
        
        print(f"{'Regular LL insert':<25} {old_timetaken:<18.6f} {'1.00x':<18}")
        print(f"{'Hybrid LL only':<25} {initial_timetaken:<18.6f} {old_timetaken/initial_timetaken:.0f}x")
        print(f"{'Hybrid Total':<25} {actual_timetaken:<18.6f} {old_timetaken/actual_timetaken:.0f}x")
        
        print("-"*70)
        overall_speedup = old_timetaken/actual_timetaken
        print(f"{'OVERALL SPEEDUP':<44} {overall_speedup:.0f}x")
        print("="*70 + "\n")
        
testcase1()
testcase2()
testcase3()
testcase4()