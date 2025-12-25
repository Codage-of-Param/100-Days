# **Stack**



* A stack is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle—the last element added is the first one removed.
  
* Visualise as stack of plates: you add and remove from the top.



>> There are many implementation :



1. List:

	- Time Complexity :
   
   		Push : O(n)
   
   		Pop : O(1)

   		Peek : O(1)

   		is\_empty : O(1)

 		search : O(n)

   **Note** : pop(0) would be O(n) (not used for stack).
   
3. Class

   - Time Complexity :
   
		Push : O(n)

     	Pop : O(1)

     	Peek : O(1)

     	is\_empty : O(1)

     	search : O(n)
     
   **Note** : Class abstraction **improves readability and safety**, not performance.
   
5. Collection deque

	- Time Complexity :
	
		Push : O(1)

   		Pop : O(1)

   		Peek : O(1)
	
		is\_empty : O(1)

   		search : O(n)



*  **Common Use Cases:**



* **Undo/Redo functionality**: Each action gets pushed onto a stack, and undoing pops from it.



* **Browser** **history**: Back button pops from the history stack.



* **Expression evaluation**: Converting infix to postfix notation or evaluating expressions.



* **Depth-first search (DFS)**: Traversing graphs or trees.



* **Balanced parentheses**: Checking if brackets/parentheses are properly matched.



##### ***In Short :***



=> Use **list for simplicity**, **deque for production-grade stacks**, and **class-based stacks for conceptual clarity**.

