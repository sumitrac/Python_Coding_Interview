#manually creating a linked list 

# Nodes
# 1. Value - anything strings, integers, objects
# 2. The Next Node 

class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value 
        self.nextNode = nextNode

# create nodes containing "3" "5" "7" "10"
node1 = LinkedListNode("3")
node2 = LinkedListNode("Apples")
node3 = LinkedListNode("7")
node4 = LinkedListNode("Oranges")

node1.nextNode = node2 # "3" -> "5"
node2.nextNode = node3  # "5" -> "7"
node3.nextNode = node4 # "7" -> "10"

# node1 -> node2 -> node3 - node4 
currentNode = node1 #current node is head 
while True:
    print(currentNode.value, "->", end=" ")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode



