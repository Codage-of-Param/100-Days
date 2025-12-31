# Question from Leetcode - https://leetcode.com/problems/asteroid-collision/

# Time Complexity = Space Complexity = O(n)

def asteroidCollision(asteroids):
        stack = []
    
        for i in asteroids:
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
    
asteroid_list = []
n = int(input("Enter length of asteroids : "))

for i in range(n):
    elem = int(input(f"Enter asteroid {i+1} position : "))
    asteroid_list.append(elem)
    
final = asteroidCollision(asteroid_list)

print("After all collisions : ", final)