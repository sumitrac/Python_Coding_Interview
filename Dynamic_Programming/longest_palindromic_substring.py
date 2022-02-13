# Maximum Subarray 

# Given an integer array nums, find the contiguous subarray (containing at least one number)
#  which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
nums1 = [1]
# Output: 1
nums2 = [5,4,-1,7,8]
# Output: 23

def max_sum(array):
    max_till_now = array[0]
    max_ending = 0

    for i in range(0, len(array)):
        max_ending += array[i]
        if max_ending < 0:
            max_ending = 0

        elif max_till_now < max_ending:
            max_till_now = max_ending
    return max_till_now

print(max_sum(nums))
print(max_sum(nums1))
print(max_sum(nums2))
