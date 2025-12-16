# Reverse an array
# Que from : https://www.hackerrank.com/challenges/arrays-ds/problem

n = int(input("\nEnter a length of an array : "))
array=[]

for i in range(n):
    element = int(input(f"Enter element {i+1} : "))
    array.append(element)
    
print(array)
array.sort()
print(array)

first = 0
last = n-1


while(first<last):
    array[last], array[first] = array[first], array[last]
    first += 1
    last -= 1

print(array)