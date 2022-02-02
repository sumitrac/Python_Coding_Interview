# Implement a function, find_product(lst), which modifies a list so 
# that each index has a product of all the numbers present in the list 
# except the number stored at that index.

nums = [1,2,3,4]
# output = [24,12,8,6]

nums1 = [4,2,1,5,0]
# output = [0,0,0,0,40]

def productSum(array):
    '''
    input is array 
    output is products of all nums in array expect the num in the index 
    '''
    # get the product of all all sides
    # get the product of all right sides 
    # multiply two product and place in same indexes 

    products = []
    left_product = 1

# nums = [1,2,3,4]
    for ele in array:
        products.append(left_product)
        left_product *= ele  # [1,1,2,6]

    right_product = 1
    for ele in range(len(array) -1, -1, -1):
        products[ele] *= right_product
        right_product *= array[ele]

    return products 

print(productSum(nums))

# Time: O(N)
# Space: O(N)
