# 2 Pointer Interesting Easy level question !  
# QUESTION LINK : https://unstop.com/code/practice/250137

def find_sum_eq_t(arr, t):
    left = 0
    right = len(arr) - 1
    print(arr)
    while left < right:
        
        current_sum = arr[left] + arr[right]
        
        if current_sum == t:
            return left, right
        
        elif current_sum < t:
            left += 1
        
        else:
            right -= 1


n = int(input("Enter types of Flower : "))
t = int(input("Flowers needed is : "))

arr = []

for i in range(n):
    val = int(input("Enter an element: "))
    arr.append(val)

arr = sorted(arr)

res = find_sum_eq_t(arr, t)
print(res)

'''
Check:
-> When i wrote this code first time i faced 4 failed testcases which is of wrong loop and the main issue i faced that was the multiple answers possible for one array
'''
