# Implement a function findMinimum(lst) 
# which finds the smallest number in the given list.

input = [9, 2, 3, 6]
# output = 2
input1=[2, 4, 0, 7]
# output = 0

def minValue(array):
    '''
    compare each element with each other
    '''
    min = array[0] 
    for i in array:
        if i < min:
            min = i
    return min 

print(minValue(input))
print(minValue(input1))

# Time: O(N)
# Space: O(1)