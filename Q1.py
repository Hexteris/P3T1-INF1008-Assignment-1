import time
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Standard Linked List implementation
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Append values for testing
    def append(self, value):
            newNode = Node(value)
            if self.head is None:
                self.head = self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode

    #Worst case: O(n)
    def get(self, position):
        start_time = time.process_time()
        currNode = self.head
        for i in range(position):
            currNode = currNode.next
        end_time = time.process_time()
        timeTaken = end_time-start_time
        return currNode.data, timeTaken

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
        timeTaken = end_time-start_time
        return timeTaken

    #Worst case: O(n)
    def delete(self, position):
        start_time = time.process_time()
        currNode = self.head
        for i in range(position):
            currNode = currNode.next
        currNode.next = currNode.next.next
        end_time = time.process_time()
        timeTaken = end_time-start_time
        return timeTaken

    def printAll(self):
        if self.head != None:
            currNode = self.head
            while currNode.next != None:
                print(currNode.data)
                currNode = currNode.next
            print(currNode.data)



#Hybrid Linked List implementation
class ModifiedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.array = []

    #Append values for testing
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
        start_time = time.process_time()
        if position < 0 or position > len(self.array):
            print("Position out of bounds")
        else:
            end_time = time.process_time()
            timeTaken = end_time-start_time
            return self.array[position].data, timeTaken


    def insert(self, position, value):
        #time taken for node to be added to linked list
        timeTaken = 0 
        #total time taken for node to be added and array to be updated
        totalTimeTaken = 0 
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
            timeTaken = end_time-start_time


            #adds new node into auxiliary array
            self.array.insert(position, newNode)

        #Calculate time taken for node to be added to linked list AND array
        end_time = time.process_time()
        totalTimeTaken = end_time-start_time

        return timeTaken, totalTimeTaken


    #O(1)
    def delete(self, position):
        if position < 0 or position > len(self.array):
            print("Position out of bounds")
        elif position == 0:
            self.head = self.head.next
            self.array.pop(position)
        else:
            #time taken for node to be removed from linked list
            timeTaken = 0 
            #total time taken for node to be removed from LL and array
            totalTimeTaken = 0 

            #starts timer after node is created
            start_time = time.process_time() 

            targetNode = self.array[position-1]
            targetNode.next = targetNode.next.next

            #Calculate time taken for node to be removed from linked list
            end_time = time.process_time()
            timeTaken = end_time-start_time

            self.array.pop(position)
            #Calculate time taken for node to be added to linked list AND array
            end_time = time.process_time()
            totalTimeTaken = end_time-start_time

            return timeTaken, totalTimeTaken

    def printAll(self):
            currNode = self.head
            while currNode:
                print(currNode.data, end=" -> " if currNode.next else "")
                currNode = currNode.next
            print()



#TEST CASES 1-4
def testcase1():
    print("\n=== Test Case 1: GET ===")
    testList = ModifiedLinkedList()
    testList.append("A")
    testList.append("B")
    testList.append("C")
    testList.append("D")
    print("List contents:", end="")
    testList.printAll()

    # Test getting valid positions
    print(f"Get index 0: {testList.get(0)[0]}")
    print(f"Get index 2: {testList.get(2)[0]}")  
    print(f"Get index 3: {testList.get(3)[0]}")  
    
    # Test getting invalid positions
    print(f"Get index -1: {testList.get(-1)}")  
    print(f"Get index 10: {testList.get(10)}") 

def testcase2():
    print("\n=== Test Case 2: INSERT ===")
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
    print("\n=== Test Case 3: DELETE ===")
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

def testcase4(noOfTestCase):
    print("\n=== Test Case 4: Performance Comparison ===")

    #EDIT NUMBER OF TEST RECORDS HERE
    print(f"Testing with {noOfTestCase} records")   

    oldList = LinkedList()
    modifiedList = ModifiedLinkedList()

    print("Generating records...\n")
    for i in range(noOfTestCase):
        oldList.append(Node(i))
        modifiedList.append(Node(i))
    
    #Running Insert operation
    print("Calculating insert time for regular linked list...")
    #Test insert at 80% of total records index
    regularTimeInsert = oldList.insert(round(noOfTestCase * 0.8), "x")
    print("Calculating insert time for hybrid linked list...\n")
    hybridTimeInsert, totalHybridTimeInsert = modifiedList.insert(round(noOfTestCase * 0.8), "x")

    #Running Delete operation
    print("Calculating delete time for regular linked list...")
    regularTimeDelete = oldList.delete(round(noOfTestCase * 0.8))
    print("Calculating delete time for hybrid linked list...\n")
    hybridTimeDelete, totalHybridTimeDelete = modifiedList.delete(round(noOfTestCase * 0.8))

    #Running Get operation
    print("Calculating get position time for regular linked list...")
    regularTimeGet = oldList.get(round(noOfTestCase * 0.8))
    print("Calculating get position time for hybrid linked list...\n")
    hybridTimeGet = modifiedList.get(round(noOfTestCase * 0.8))

    print("\n" + "="*70)
    print("                    PERFORMANCE COMPARISON RESULTS")
    print("="*70)
    print(f"{'INSERT Operation':<25} {'Time (s)':<12} {'Speedup vs Regular':<18}")
    print("-"*70)
    
    print(f"{'Regular LL INSERT':<25} {regularTimeInsert:<18.6f} {'1.00x':<18}")
    print(f"{'Hybrid LL Only':<25} {hybridTimeInsert:<18.6f} {regularTimeInsert/hybridTimeInsert:.0f}x")
    print(f"{'Hybrid Total':<25} {totalHybridTimeInsert:<18.6f} {regularTimeInsert/totalHybridTimeInsert:.0f}x")
    
    print("-"*70)
    overall_speedup = regularTimeInsert/totalHybridTimeInsert
    print(f"{'OVERALL INSERT SPEEDUP':<44} {overall_speedup:.0f}x")
    print("="*70 + "\n")


    print(f"{'DELETE Operation':<25} {'Time (s)':<12} {'Speedup vs Regular':<18}")
    print("-"*70)
    
    print(f"{'Regular LL DELETE':<25} {regularTimeDelete:<18.6f} {'1.00x':<18}")
    print(f"{'Hybrid LL Only':<25} {hybridTimeDelete:<18.6f} {regularTimeDelete/hybridTimeDelete:.0f}x")
    print(f"{'Hybrid Total':<25} {totalHybridTimeDelete:<18.6f} {regularTimeDelete/totalHybridTimeDelete:.0f}x")
    
    print("-"*70)
    overall_speedup = regularTimeDelete/totalHybridTimeDelete
    print(f"{'OVERALL DELETE SPEEDUP':<44} {overall_speedup:.0f}x")
    print("="*70 + "\n")


    print(f"{'GET Operation':<25} {'Time (s)':<12} {'Speedup vs Regular':<18}")
    print("-"*70)
    
    print(f"{'Regular LL GET':<25} {regularTimeGet[1]:<18.6f} {'1.00x':<18}")
    print(f"{'Hybrid GET':<25} {hybridTimeGet[1]:<18.6f} {regularTimeGet[1]/hybridTimeGet[1]:.0f}x")
    
    print("-"*70)
    overall_speedup = regularTimeGet[1]/hybridTimeGet[1]
    print(f"{'OVERALL GET SPEEDUP':<44} {overall_speedup:.0f}x")
    print("="*70 + "\n")

def main():

    if len(sys.argv) > 1:
        try:
            noOfRecords = int(sys.argv[1])
        except ValueError:
            print("Please input only integers")
            return
    else:
        noOfRecords = 1000000

    testcase1()
    testcase2()
    testcase3()
    testcase4(noOfRecords)


if __name__ == "__main__":
    main()
