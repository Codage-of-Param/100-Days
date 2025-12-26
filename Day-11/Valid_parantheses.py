
'''
 Valid parantheses : https://leetcode.com/problems/valid-parentheses/description/ Using stack!

Time complexity = Space complexity = O(n) 
'''

def checking(stack, parantheses, paranthese_dictionary):
    for ch in (parantheses):
        if ch in paranthese_dictionary:
            if stack and stack[-1] == paranthese_dictionary[ch]:
                stack.pop()
                
            else:        
                return False
        else:
            stack.append(ch)
        
    return True if not stack else False

stack = []
parantheses = input("Enter a string of parantheses: ")

paranthese_dictionary = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

Valid = checking(stack, parantheses, paranthese_dictionary)    
   
print("It is Valid ? ", Valid)    

'''
CONCEPT:

- It Simply done by a hash concept and the stack concept
- We check parantheses from the top and if (top-1) element is match with the hash(dictionary) then it ignore those paor of parantheses because it's a valid pair and check for next.
'''
