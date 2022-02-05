# Given an integer list, return the maximum sublist sum. 
# The list may contain both positive and negative integers and is unsorted.

# Kadane's Algorithm / This algorithm takes a dynamic programming approach to solve the maximum sublist sum problem 
# sliding window concept 

input = [ -4, 2, -5, 1, 2, 3, 6, -5, 1]
# output = 12  --> 1+2+3+6

def maxSum(array):
    # assign 
    current_max = array[0]
    global_max = array[0]

    for i in range(1, len(array)):
        if current_max < 0:
            current_max = array[i]
        else:
            current_max += array[i]
        
        if global_max < current_max:
            global_max = current_max
    return global_max

print(maxSum(input))