# Prefix sum method

# Time complexity O(n) # because 3 loops
# Space complexity O(n) because 2 list arr and prefix 
arr = []
count=0

n = int(input("\nEnter array length : "))
k = int(input("Enter the sum for subsequent array : "))
print("\n")

for i in range(n):
    elem = int(input(f"Enter an element {i+1}: "))
    arr.append(elem)
    
prefix = []
p1 = 0 
p2 = p1+1

while (p2<(len(arr))):
    prefix.append(arr[p1]+arr[p2])
    p1+=1
    p2+=1

print(prefix)

for i in prefix:
    if i==k:
        count+=1


print(f"\nTotal Subarray whose sum is {k} is {count}")  

'''
-> It is less efficient because we only need count value whose sum is k.
-> we don't need all consequent array element sum
'''