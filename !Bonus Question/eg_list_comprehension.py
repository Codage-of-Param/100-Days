# Write a multiplication table with using List comprehension

# approach 1 : With list

number = int(input("Enter a number for table: "))
i=[1,2,3,4,5,6,7,8,9,10]
table = [number*j for j in i]
print(table)


# approach 1 : Without list
number = int(input("Enter a number for table: "))
table = [number*j for j in range(1,11)]
print(table)
