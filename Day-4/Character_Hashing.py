# Time Complexity : O(n+m)
# Space Complexity : O(1) because of fixed size of hash_list

'''
Constraint : a <= n[i] <= z
'''

n = ['a','z','y','u','y','y','z','a','a','a']
m = ['d','a','y','u']

hash_list = [0]*26 # Because 25 characters are there
answer_list = []

print("\nn list : ",n)
print("m list : ",m)

for ch in n:
    asccii = ord(ch) # Generates a asccii value
    idx = asccii - 97 # If 0 then a , 1 then b ,.....
    hash_list[idx] += 1
print("\nAfter counting of n : ",hash_list)

for ch in m:
    asccii = ord(ch) 
    idx = asccii - 97
    answer_list.append(hash_list[idx])
    
print("Counting of m w.r.t n list is ",answer_list,"\n")

'''
FURTHER EXPIREMENTS I CAN DO IS:

1. Take User inputs
2. Validate it
3. Do it for both CAPITAL & small Alphabets

'''