# PLUS ONE PROBLEM
# From : https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array

from functools import reduce

numbers = []

n = int(input(f"Enter length: "))

for i in range(n):
    item = int(input(f"Enter an item {i+1} : "))
    numbers.append(item)

result = reduce(lambda x, y: x * 10 + y, numbers) # Here, x is a current number and y is a next number of current number

final_ans = result+1
size = len(str(final_ans))

Answer = []

while(size!=0):
    rem = final_ans%10
    Answer.append(int(rem))
    final_ans/=10
    size-=1

Answer.reverse()
print("After Plus one the new list is : ",Answer)


