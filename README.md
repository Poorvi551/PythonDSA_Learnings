# PythonDSA_PentagonSpace

## Table of Contents

1. [Time complexity](#time-complexity)
2. [Space complexity](#space-complexity)
3. [Searching Algorithm](#searching-algorithm)
4. [Sorting Algorithm](#sorting-algorithm)
   
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

      def binary_search(l,key):
          st=0
          end=len(l)+1
          while st<=end:
             mid = st + end // 2
             if key==l[mid]:
                return mid
             elif key<l[mid]:
                end=mid-1
             else:
                st=mid+1
           return -1
      l=eval(input("Enter the sorted collection:"))
      key=int(input("Enter the key: "))
      print(binary_search(l,key))

## 3. Ternary Search

* It is a searching algorithm which works on sorted collection by repeatedly dividing the collection into 3 parts.

* Algorithm :-

  1. Consider two pointers
        * li=0
          
        * hi=len(col)-1
  2. Run the loop until li>hi
  3. Find the mid values
        * mid1 = li+(hi-li)//3
          
        * mid2 = hi-(hi-li)//3
  4. If mid1 value == targeted element, return index of mid1 value.
     If mid2 value == targeted element, return index of mid2 value.
  5. If key < next val

*  *Source code :- [ternarysearch](./ternarysearch)*
```# Ternary Search

def ternary_search(col,key):
    li=0
    hi=len(col)-1
    while li<=hi:
        mid1=li+(hi-li)//3
        mid2=hi-(hi-li)//3
        if key==col[mid1]:
            return mid1
        if key==col[mid2]:
            return mid2
        if key<col[mid1]:
            hi=mid1-1
        elif key>col[mid2]:
            li=mid2+1
        else:
            li=mid1+1
            hi=mid2-1
    return -1
col=eval(input("Enter collection:"))
key= int(input("Enter the value:"))
print(ternary_search(col,key))
```

## Sorting Algorithm 

* It is used to arrange the values either in ascending or descending order.
* There are some type of sorting algorithm:

   1. Bubble sort
   2. Selection sort
   3. Insertion sort
   4. Quick sort
   5. Merge sort

## 1. Bubble Sort :

* It is the sorting algorithm where each and every element will get *swapped* based on condition in order to sort the values.
* It performs n-1 passes to arrange the values.
* In each and every pass, the sorted element will be at the last.

* Steps :

1. Consider the collection
2. Consider the starting value.
3. Compare current value is greater than swap it or else keep as it is
4. Consider the next pair of elements and repeat step 3 and step 4 until the value is sorted.
5. After one complete pass, the largest element will be at the last.
6. repeat the same steps for remaining values by ignoring the last sorted one. 

* Source code :- [bubblesort](./bubblesort)
```
def bubble_sort(col):
    for i in range(1,len(col)):
        for j in range(0,len(col)-i):
            if col[j]>col[j+1]:
                col[j],col[j+1]=col[j+1],col[j]
    return col
col=eval(input("Enter collection:"))
print(bubble_sort(col))
```

