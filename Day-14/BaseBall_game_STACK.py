# Question from :  https://leetcode.com/problems/basebal-game/

output=[]

# ops_stack = ["5","2","C","D","+"]
# ops_stack = ["1","C"]
ops_stack = ["5","-2","4","C","D","9","+",'+']

for ch in ops_stack :
    if ch=="C":
        output.pop()
        
    elif ch=="D":
        double = int(output[-1])*2
        output.append(double)
        
    elif ch=="+":
        add = int(output[-1]) + int(output[-2])
        output.append(add)
    
    else:
        output.append(int(ch))
        
print(sum(output))


# Time complexity O(n)
