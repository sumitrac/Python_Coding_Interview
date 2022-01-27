# Implement a function that removes all the even elements from a given list. 
# Name it remove_even(lst).

my_list = [1,2,4,5,10,6,3]
# Output: [1,5,3]

def removeEven(lis):
    '''
    Input: A list with random integers.
    Output: A list with only odd integers

    Iterate through the list
    remove all int that is divisible by 2 
    return remindering integers 
    '''
    nums = []
    for i in lis:
        if i % 2 != 0:
            nums.append(i)
    return nums

print(removeEven(my_list))
# Time: O(N)
# Space: O(N)
# could you do it with constant space? 

