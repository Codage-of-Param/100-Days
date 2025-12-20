n = ['a','u','y','y','z','A','R','W','A']
m = ['D','a','y','u','A']

hash_list = [0]*51 
answer_list = []

print("\nn list : ",n)
print("m list : ",m)

for ch in n:
    asccii = ord(ch)
    
    if (65 <= asccii <= 90):
        idx = asccii - 65 
        hash_list[idx] += 1
        
    elif (97 <= asccii <= 122):
        idx = asccii - 97 + 25 
        hash_list[idx] += 1
print("\nAfter counting of n : ",hash_list)

for ch in m:
    asccii = ord(ch) 
    if (65 <= asccii <= 90):
        idx = asccii - 65 
        answer_list.append(hash_list[idx])
        
    elif (97 <= asccii <= 122):
        idx = asccii - 97 + 25 
        answer_list.append(hash_list[idx])
    
    else:
        answer_list.append(0)
    
    
print("Counting of m w.r.t n list is ",answer_list,"\n")
