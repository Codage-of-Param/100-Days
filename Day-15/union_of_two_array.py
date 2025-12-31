'''
QUESTION :  Union of two arrays [EASY]

- Three methods:
    1. Brute force with O(n^2)
    2. Sorting the arrays with O(nlogn)
    3. Hashing with O(n)

Method-3:
    Time complexity : O(n)
    Space complexity : O(n)
'''

def user_input():
    arr=[]
    n = int(input("Enter length of array : "))
    
    for i in range(n):
        elem = int(input(f"Enter element {(i+1)} : "))
        arr.append(elem)
        
    return arr

arr1 = user_input()
arr2 = user_input()

hash_set = {}

for i in arr1:
    if i not in hash_set:
        hash_set[i] = 1
        
for j in arr2:
    if j not in hash_set:
        hash_set[j] = 1
    

print(f'Total number of unique elements[UNION] are/is {len(hash_set)}')
print(f'Elements are/is {hash_set.keys()}')
