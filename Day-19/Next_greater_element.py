# NEXT GREATER ELEMENT : Return the next and immediate greater element, If it is not put -1

# - Time Complexity: O(n)
# - Space Complexity: O(n)

arr = []

n = int(input("Enter length of an array: "))

for i in range(n):
    elem = int(input(f"Enter element {i+1} : "))
    arr.append(elem)

stack = []
ans = []

i = len(arr)-1

for i in reversed(arr):
    
    while (stack and (stack[-1]<=i)):
        stack.pop()
        
    if len(stack)==0:
        ans.append(-1)
    else:
        ans.append(stack[-1])
    
    stack.append(i)

ans.reverse()
print(f"Original array : {arr}")
print(f"Next Greater element array : {ans}")
