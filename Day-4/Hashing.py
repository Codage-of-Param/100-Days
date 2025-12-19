# Time Complexity : O(n+m)
# Space Complexity : O(1) because of fixed size of hash_list

'''
Constraints :

1 <= n[i] <= 10
n can have 10 CR elements (10^8)
m can have 10 CR elements (10^8)
'''
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,11,1,9,5,20,2]

hash_list = [0]*11 # Why 11? becuase index starts from 0
answer_list = []

print("\nn list : ",n)
print("m list : ",m)

for i in n:
    hash_list[i] += 1
print("\nAfter counting of n : ",hash_list)

for i in m:
    if (i<1) or (i>10):
        answer_list.append(0)
    else:
        answer_list.append(hash_list[i])
        
print("Counting of m w.r.t n list is ",answer_list,"\n")

'''
FURTHER EXPIREMENTS I CAN DO IS:

1. Take User inputs
2. Validate it

'''