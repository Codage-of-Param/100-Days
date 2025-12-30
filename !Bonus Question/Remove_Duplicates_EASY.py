#Que from : https://leetcode.com/problems/contains-duplicate/

# REMOVE DUPLICATES USING HASH SET

# Time complexity : O(n)
# Space complexity : O(1)

list_num = [1,2,3,1]

hash_set = set() 

for n in list_num: 
    if n in hash_set:
        print("Contains Duplicate")
    hash_set.add(n)
            
'''
- we made set because set stores only unique values so duplicates will be automatically removed 

- Another method is Sort the list and make a loop for decision 
- but it's time complexity is O(nlogn) that's why we don't use it
'''

