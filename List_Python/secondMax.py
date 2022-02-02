# Second largest element in the list

input = [5, 10, 20]
# output = 10

# Tracersing the list twice 
# find first max 
# find second max 
def secondMax(array):
    '''
    input nums of array
    output second max
    first first max 
    find second max 
    '''
    firstMax = float('-inf')
    secondMax = float('-inf')

    for num in array:
        if num > firstMax:
            firstMax = num

    for num in array:
        if num != firstMax and num > secondMax:
            secondMax = num
    return secondMax

print(secondMax(input))
# Time: O(N)
# Space: O(1)

