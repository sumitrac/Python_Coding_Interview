# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such 
# that the 0th index will have the largest number, the 1st index will have the smallest, 
# and the 2nd index will have second-largest, and so on. In other words, 
# all the even-numbered indices will have the largest numbers in the list in descending order and 
# the odd-numbered indices will have the smallest numbers in ascending order.

lst = [1,2,3,4,5] #input is already sorted 
# output = [5,1,4,2,3]

def reArrange(array):
    '''
    array is already in 
    store first and last element to new list 
    return new list 
    '''
    new = []
    # array.sort()
    # print(array)
    #iterating half the list
    for num in range(len(array)//2):
        #append corresponding last element
        new.append(array[-(num+1)])
        #append current element
        new.append(array[num])

    if len(array) % 2:
        #if middle value then append 
        new.append(array[len(array)//2])
    return new 

print(reArrange(lst))
# print(5//2)
# print(5%2)

# Time: O(N)
# Space: O(N)

