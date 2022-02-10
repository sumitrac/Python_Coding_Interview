# There is a programming language with only four operations and one variable x:
# ++X and X++ increments the value of the variable x by 1:
# --x and x-- decrements the value of the variable x by 1:

# initially, the value of x is 0

# Given an array of strings operations containing 
# a list of operations, returns the final value of x after performing all the operations

operations = ["--X", "X++", "X++"]
# output = 1

# start count = 0
# iterate through each string in array
# check if sting, increment or decrements bases on that

def find_value_after_operations(operations):
    value = 0
    for i in operations:
        if i == "--X" or i == "X--":
            value -= 1
        if i == "X++" or i == "++X":
            value += 1
    return value 
print(find_value_after_operations(operations))

        
