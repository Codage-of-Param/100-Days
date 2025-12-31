# Que from : https://leetcode.com/problems/asteroid-collision/description/

'''
Constraints: 

1. 2 <= asteroids.length <= 104
2. -1000 <= asteroids[i] <= 1000
3. asteroids[i] != 0
'''

# Time complexity : O(n)
# Space complexity : O(n)

def Asteroid_Collisions(asteroid_position):
    stack = []
    
    for i in asteroid_position:
        while stack and stack[-1]>0 and i<0:
            diff = i + stack[-1]
            
            if diff<0:
                stack.pop()
                
            elif diff>0:
                i = 0
                
            else:
                i = 0
                stack.pop()

        if i:
            stack.append(i)
    
    return stack

asteroid_position = []

n = int(input("\nEnter number of asteroids : "))
print("\n")

for i in range (n):
    elem = int(input(f"Enter position of asteroid {i+1} : "))
    asteroid_position.append(elem)

finalResult = Asteroid_Collisions(asteroid_position)

print(f"\nAll asteroid positions {asteroid_position}")
print(f"State of the asteroids after all collisions : {finalResult}\n")