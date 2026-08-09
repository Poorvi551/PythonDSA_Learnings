# PythonDSA_PentagonSpace

## Table of Contents

1. [Time complexity](#time-complexity)
2. [Space complexity](#space-complexity)
3. [Searching Algorithm](#searching-algorithm)
   
## Data Structures

* **Data** - It is a rawfact (useless and useful or processed and unprocessed content)
* Informmation - is a processed content.

* **Data structures** - It is the phenomenon of storing and managing the data in a organised way.
* So that it can be accessed easily.
* It takes less time.
* Increase Efficiency of code.

  1. Time complexity
  2. Space complexity
 
## Time complexity

* It is the measure of total time taken by the program for its complete execution.
* They are of 3 ways :
  1. Best Time complexity
  2. Worst Time complexity
  3. Average Time complexity

### 1. Best Time complexity

* It is the measure of minimum time taken by the program to get positive response.

### 2. Worst Time complexity

*  It is denoted by Big O notation.

### 3. Average Time complexity

* It is the measure of average time taken by the program to get positive response.

* Conditional Statements (O(1)) - if, else
* Looping Statement O(n) - for loop
* Nested for Loop O(m*n) or O(n^2) - nested for loop

## Space complexity

* It is the measure of total space consumed by the program for its complete execution.
  
   1. **constant** -> O(1)
  
    * Ex : a=10
    * It is the measure of space consumed by one value.
  
   2. **Linear** -> O(n)
   
      * Ex:- l=[10,20,30]  
      * It is the measure of space consumed by linear data or collection data.
     
   3. **Auxiliary** -> O(1) or O(n)
      
   * Ex : out =[] -> O(1), out=[10,20,30] -> O(n)
   * It is the temporary space consumed by a temporary variable.

## Searching Algorithm

* It is the algorithm which is used to check whether the value is present in collection or not.
* If the value is present , we will return the index of the value.
* If value is not present , we return -1.

* They are of 3 types :

  1. Linear search
  2. Binary search
  3. Ternary search
 
## 1. Linear Search

* It is a searching algorithm which works on the principle called sequential principle.
* It will traverse through the collection to find the targeted element.
* *Ex :- Source code : [linearsearch.py](./linearsearch.py)*

      def linear_search(col,key):
      for i in range(len(col)):
          if col[i]==key:
              return i
      return -1
      col=eval(input("Enter list:"))
      key=int(input("Enter key val:"))
      print(linear_search(col,key))

## 2. Binary Search

* It is a searching algorithm which works on sorted collection by repeatedly , dividing the collection into two halves until we found targeted element.
* *Ex :- Source code :-[binarysearch.py](./binnarysearch.py)*

  
  
