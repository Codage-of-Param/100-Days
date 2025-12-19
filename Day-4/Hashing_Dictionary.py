n = [5,3,2,2,1,5,5,7,5,10]
m = [10,11,1,9,5,20,2]

hash_dict = {}
answer_list = []

print("\nn list : ",n)
print("m list : ",m)

for i in n:
    if(i not in hash_dict.keys()):
        hash_dict.update({i : 1})
    else:
        hash_dict.update({i : hash_dict.get(i)+1})
print("\nAfter counting of n : ",hash_dict)

for i in m:        
    if hash_dict.get(i)==None:
        answer_list.append(0)
    else:
        answer_list.append(hash_dict.get(i))
        
print("Counting of m w.r.t n list is ",answer_list,"\n")
        
'''
FURTHER EXPIREMENTS I CAN DO IS:

1. Take User inputs
2. Validate it

'''