# Majority element : https://leetcode.com/problems/majority-element/
# Element must be present >(n/2) times

'''
There are 3 methods for finding majority element

1. Brute force method => TC is O(n^2)
2. Better method (with sorting) => TC is O(nlogn)
3. Moore's algo => TC is O(n)
'''

array = [1,2,3]
n = len(array)
freq = 0
ans = 0

for i in array:
    
    if freq==0:
        ans = i
    if ans==i:
        freq+=1
    else: 
        freq-=1

count = 0 # For checking majority element is there or not if arr[1,2,3] then it returns 3 but logically it's not the right answer

for i in array:
    if i==ans:
        count+=1
    else:
        count=count+0
if count>(n/2):
    print(ans)
else:
    print("No majority element in an array")
    
