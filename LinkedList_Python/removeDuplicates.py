head = [1, 1, 2]
# output = [1,2]

def removeDuplicates(head):
    newList = []
    while head:
        if head.next not in newList:
            newList.append(head.next)
    return newList

print(removeDuplicates(head))