# **What the Problem Is ?**

  - You need to design a ***special stack that supports these four operations in constant time (O(1))*** : 

    - push(val) — Add a number to the stack

    - pop() — Remove the top number

    - top() — Look at the top number

    - getMin() — Get the minimum number currently in the stack

The challenge is making getMin() fast — you can’t scan through the stack each time because that would take linear time (O(n)).

# **Two Optimal Ways to Implement a Min Stack**

  * **Approach 1 - Two Stacks (Main + Min Stack)**<br>
      - You maintain *two stacks simultaneously*: 

        1. Main_Stack — Stores all elements<br>
        2. Min_Stack — Stores the minimum at every stage
       
        **Rules**:

        * **On push(val)**:

          - Push val into mainStack.

          - In minStack, push the smaller of val and current min.
      
          - (So minStack always mirrors the min at each level in mainStack.) 

        * **On pop()**:

          - Pop from mainStack

          - Also pop from minStack

          - (This keeps them synchronized.) 

        * **top()** — Return the top of mainStack

        * **getMin()** — Return the top of minStack (which is the current minimum) <br>
Because minStack always holds the minimum up to this point, you get the current minimum in O(1) time.

      ### **Why this Works?**

    - A stack alone can do **push/pop/top in O(1)**, but **not getMin()**.<br>
    
    - If we remember the minimum along with every element (pair or minStack), then the minimum at any point is always at the top. So all operations can be done in constant time

      ### **Complexity Summary**:

      | Operation | Time Complexity | Why                                     |
      | --------- | --------------- | --------------------------------------- |
      | push      | O(1)            | Simple stack push                       |
      | pop       | O(1)            | Simple stack pop                        |
      | top       | O(1)            | Peek top of stack                       |
      | getMin    | O(1)            | Top of min information always available |

      ### **CODE** :
      
      - [Implementation](https://github.com/Codage-of-Param/100-Days/blob/main/!Bonus%20Question/Min%20Stack/Min_stack_2_stacks.py)
      
      ### **🔑 Key Points (Quick Revision)**
      
        - stack → stores actual values

        - Min_Stack → stores minimum value till that index

        - Both stacks always stay same size

        - getMin() is always O(1) because minimum is at the top of min_stack
      ---

  * **Approach 2 - One Stack + One Variable**

    **Core Idea:**

      - We maintain:

          - One normal stack

          - One variable min_val (current min)

    - When a new minimum arrives, we do not push it directly.<br>
    - Instead, we push a calculated encoded value that helps us restore the previous minimum later.

    => This **encoding** allows us to:

      - Track minimum in O(1)

      - Use O(1) extra space (only one variable)
   
    **Key Insight**:
    
    - When **pushing a value smaller than the current minimum**, we:

        - Encode the value

        - Update current_min

    - When **popping, if we see an encoded value**:

        - We decode it

        - Restore the previous minimum

        - So the stack itself helps us remember past minimums.
     
    ### ***Encoding Formula (Very Important)***:

    - When `x < current_min` :<br>
    
    ```py
        encoded_value = 2*val - current_min # val is pushed element by user
     ```

    Then:<br>
    ```current_min = val```

    - This **encoded value is always less than the new minimum.**

    ### ***Decoding Formula***: (during pop)

    - If `popped value < current_min` , it means:

      - This value is encoded

      - The real value was current_min

    - Previous minimum is restored using:
   
      ```py
          previous_min = 2*current_min - encoded_value
      ```

      ### **Why This Works ?**

        - Normal values are ≥ current minimum

        - Encoded values are always smaller than the current minimum

        - This difference lets us identify encoded values safely

        - Mathematical transformation preserves history

     ### **CODE** :

    - [Implementation](https://github.com/Codage-of-Param/100-Days/blob/main/!Bonus%20Question/Min%20Stack/Min_stack.py)
      
📌  ***In shoert (One Line)***:<br>
- We use a mathematical encoding technique to store previous minimums inside the stack itself, allowing getMin() in O(1) time using only one extra variable.

