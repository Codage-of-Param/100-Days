'''
Question : Find Itinerary from Tickets

INPUT: from        to
    {"Chennai" : "Bengaluru",
    "Mumbai" : "Delhi",
    "Goa" : "Chennai",
    "Delhi" : "Goa"}
    
OUTPUT:
    "Mumbai", "Delhi", "Goa", "Chennai", "Bengaluru"
    
Constraints:
    - No Multiple path from single From or To
    - No loop forms
    - One From and One To
    
TIME COMPLEXITY = SPACE COMPLEXITY = O(n)
'''
# find Start : start is mumbai , no one can come in mumbai

def Start(Travel):
    # Find Start : 
        # First reverse the Travel
        # Check the which key is not present in reverse array
        # This key is Our start point  
        
    reverse_Travel = {v : k for k, v in Travel.items()}
    
    for keys in Travel:
        if (reverse_Travel.__contains__(keys)==False):
            return keys
            
def travel(Start,Travel):
    while(Travel.__contains__(Start)):
        print(Start)
        Start = Travel.get(Start)
    print(Start)
    
Travel = {
    "Chennai" : "Bengaluru",
    "Mumbai" : "Delhi",
    "Goa" : "Chennai",
    "Delhi" : "Goa"
}
print(Travel)

startPoint = Start(Travel)

print(f"Our start point is {startPoint}")

travel(startPoint,Travel)
