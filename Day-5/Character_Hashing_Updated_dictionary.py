n = ['a','u','y','y','z','A','R','W','A']
m = ['D','a','y','u','A']

hash_dict = {}
answer_list = []

print("\nn list : ",n)
print("m list : ",m)

for ch in n:
    asccii = ord(ch)
    
    if(ch not in hash_dict.keys()):
        hash_dict.update({ch : 1})
    else:
        hash_dict.update({ch : hash_dict.get(ch)+1})
print("\nAfter counting of n : ",hash_dict)

for ch in m:        
    if hash_dict.get(ch)==None:
        answer_list.append(0)
    else:
        answer_list.append(hash_dict.get(ch))
        
print("Counting of m w.r.t n list is ",answer_list,"\n")
  