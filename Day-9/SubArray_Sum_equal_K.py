# Question from https://leetcode.com/problems/subarray-sum-equals-k/description/

# Brute-Force method

# Time complexity O(n)
# Space complexity O(n)

arr = []

n = int(input("\nEnter array length : "))
k = int(input("Enter the sum for subsequent array : "))
print("\n")

for i in range(n):
    elem = int(input(f"Enter an array element {i+1}: "))
    arr.append(elem)
    
hash_list = []
count=i=0

while((i+1)<len(arr)):
    if ((arr[i] + arr[i+1]) == k):
        hash_list.append(arr[i])
        hash_list.append(arr[i+1])
        count+=1
    i+=1
 
print(f"\nSub array list whose sum is {k} => {hash_list}")  
print(f"\nTotal Subarray whose sum is {k} is {count}")      