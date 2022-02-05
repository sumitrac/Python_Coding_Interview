#Linked list Node class with constructor 
class LinkedListNode:
    def __init__(self, value, nextNode=None) -> None:
        self.value = value 
        self.nextNode = nextNode 

# Linked List class 
class LinkList: 
    def __init__(self, head=None):
        self.head = head 

    def insertNode(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node 
            return 

        currentNode = self.head 
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break 
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")

printList = LinkList()    
printList.printLinkedList()
printList.insert("3")
printList.printLinkedList()

# Note: This needs some fixes 

