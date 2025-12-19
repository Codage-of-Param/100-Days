#### **Concept of Hashing:**



\- Hashing is like creating a unique, fixed-size "fingerprint" (a number or short string) for any piece of data.



##### **Example for better understanding:**



* Imagine you have a big box of books, and instead of remembering the full title of each book, you assign each one a short number (like a locker number) based on its title.​
* That number is the hash, and it lets you quickly find where the book is stored, without searching through all the books one by one.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



In coding part we do **Character \& Number** hashing problem with **LIST and DICTIONARY** :



1. **Number Hashing with LIST :**

* In this hashing, We calculate the how many time numbers occurs in list m with respect to list n.
* we make a 2 list n and m with values.
* one hash\_list of length "According to constraints". 
* and make a single empty final answer list.
* hash\_list count value of n 



**2.   Number Hashing with DICTIONARY :**

* We do same problem with dictionary because if list size too long then it's return TLE error (Time Limit Exceeded Error, It mean Time complexity is too high)
* That's why we use dictionary because dictionary has constant time complexity O(1).



**3.   Character Hashing with LIST :**

* Why we don't make the list from 0 to 127 because in this list of characters there are only small letters that's why we use 97-122 keys = 25 characters 
* First we need asccii value by ord(ch) where ch is input character
* we do -97 because our list starts from 0 if a then asci value is 97 and 97-97=0 it means a has index 0 and according to we update the hash\_list



**4.   Character Hashing with DICTIONARY :**

* SAME AS NUMBERS



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###### ***In short*** :



=> hashing is a way to turn any data into a compact, repeatable “ID” so that programs can store, find, and verify data quickly and securely.



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###### **TOOL** :



=> You can visualize the any code with ***https://pythontutor.com/visualize.html#mode=edit***







