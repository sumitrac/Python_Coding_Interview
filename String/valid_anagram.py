# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.


s = "anagram"
t = "nagaram"
# Output: true

s1 = "rat"
t1 = "car"
# Output: false

# Anagram = is a word or phrase formed by rearranging letters
# same len 
# all lower case letter and no space 

# use hash to store key: value --> char: count of char
# compare two hashes and return 

# def valid_anagram(string1, string2):

#     # string1.lower().replace(" ", "")
#     # string2.lower().replace(" ", "")

#     s_hash, t_hash = {}, {}

#     # if len(string1) != len(string2):
#     #     return False 

#     for char in string1:
#         if char in s_hash:
#             s_hash[char] += 1
#         else:
#             s_hash[char] = 1

#     for char in string2:
#         if char in t_hash:
#             t_hash[char] += 1
#         else:
#             t_hash[char] = 1

#     return string1 == string2 

def isAnagram(s, t):
        # Anagram is a word or phrase formed by rearranging the letters
        # same len 
        # lets do all lower case letter, no space
        
        # s= anagram, t = nagaram
        
        # base case, check if len is same
        # store key: value --> char: count of char
        # compare two dictionary 
        s.lower()
        t.lower()
        s_hash, t_hash = {}, {}
        
        if len(s) != len(t):
            return False 
        
        for char in s:
            #store in hash as key(char): value(count of char) pair 
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1
                
        for char in t:
            if char in t_hash:
                t_hash[char] += 1
            else:
                t_hash[char] = 1
                
        # compare the count of char in both hashes
        # for char in range(len(s_hash)):
        return s_hash == t_hash
    
    # Time: O(N+N)
    # Space: O(N)
                
print(isAnagram(s,t))
# print(valid_anagram(s,t))
# print(valid_anagram(s1,t1))
        



