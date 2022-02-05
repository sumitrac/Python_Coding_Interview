def findTarget(head, target):
    current = head;
    while current != None:
        if current.value == target:
            return True 
        current = current.next
    return False 

print(findTarget([2, 4, 5], 4))
#not working yet 
