''' 
Question from : 
https://neetcode.io/solutions/valid-anagram
'''

def valid_anagram(s,t):
    
    if len(s) == len(t):
        hash = {}
        
        for ch in s:
            if ch in hash:
                hash.update({ch : 1+(hash.get(ch,0))})
            
            else:
                hash[ch] = 1
        
        for ch in t:
            if ch in hash:
                hash.update({ch : (hash.get(ch,0))-1})
            else: 
                hash[ch] = 1    
                
        if all(value == 0 for value in hash.values()):
            return True 
        else: return False
            
    else:
        return False 
        
s = input("Enter String s : ")
t = input("Enter String t : ")

answer = valid_anagram(s,t)

if answer==True:
    print("It is valid anagram")
else:
        print("It is not valid anagram")