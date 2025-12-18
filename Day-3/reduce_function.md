### **reduce**

*  reduce is a function that takes a list (or any iterable) and collapses it down to a single value by repeatedly applying a function.


* **SYNTAX:**

from functools import reduce
result = reduce(function, iterable, initial_value)

* **How it works:**

= Takes the first two elements, applies the function to them
= Takes that result and the third element, applies the function
= Keeps going until you've processed the entire iterable
= Returns the final single value