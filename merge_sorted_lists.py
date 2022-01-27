list1 = [1,3,4,5]  
list2 = [2,6,7,8]

# arr = [1,2,3,4,5,6,7,8]

def merge_lists(lst1, lst2):
    '''
    input: two lists
    output: sorted list 
    # use two pointer i and j for two list 
    # store sorted result in third list 
    '''
    i = 0
    j = 0
    lst1_l = len(lst1)
    lst2_l = len(lst1)
    result = []

    
    while i < lst1_l and j < lst2_l:
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    while i < lst1_l:
        result.append(lst1[i])
        i += 1
    while j < lst2_l:
        result.append(lst2[j])
        j += 1

    return result 

print(merge_lists(list1, list2))

# Time: O(n+m)
# Space: O(n)
# Could you merge list2 to list1 so that you don't need to create another list 

# use just sorted() python function if the problem focus is not only to sort arrays