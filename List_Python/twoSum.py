# googl;,;lfdgoo

lst = [1,21,3,14,5,60,9,6]
k = 81
# lst = [21,60]

def twoSum(array, target):
    '''
    iterate through the array and look for difference of target - num
    return the num and difference num from array 
    '''

    for num in array:
    #     print(num) 
    # for num in range(len(array)):
    #     print(array[num])
        if target - num in array:
            return [num, target - num]
        # else:
        #     return "two numbers doesn't exist"
    
print(twoSum(lst, k))


# last = len(lst) - 1
# print(last)

# better approach is to use hash map 