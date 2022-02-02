# Implement a function rearrange(lst) which rearranges the elements such 
# that all the negative elements appear on the left and positive elements appear at the right of the list. 
# Note that it is not necessary to maintain the sorted order of the input list.

input = [10,-1,20,4,5,-9,-6, 0]
# Output = [-1,-9,-6,10,20,4,5]

def reArrange(array):
    '''
    iterate through the list 
    store all negative nums in a list
    store all positive nums in a list
    return combine two list 
    '''
    positive = []
    negative = []

    for num in array:
        if num < 0:
            negative.append(num)
        else: 

    # for num in array:
    #     if num >= 0:
            positive.append(num)

    return negative + positive

print(reArrange(input))
# Time: O(N)
# Space: O(N)