# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Merge Sort
Best Case: O(nlogn)
Average Case: O(nlogn)
Worst Case: O(nlogn)
Space Complexity: O(n)
Stability: Yes
"""    
    
def MergeSort(arr):
    if len(arr) > 1:
         m = len(arr)//2 # int division cause if its odd
         # Split the array into two temporary arrays
         left = arr[:m]
         right = arr[m:]
         
         MergeSort(left) # Woah Recursion
         MergeSort(right) # Woah getting fancy, double recursion
         
         i = 0 # index for left
         j = 0 # index for right
         k = 0 # index for arr
         
         # Inserts smallest into the array and keeps goin till one runs out
         while i<len(left) and j<len(right):
             if left[i] < right[j]:
                 arr[k] = left[i]
                 i += 1
             else:
                 arr[k] = right[j]
                 j += 1
             k += 1
         
         # Finish off the array that had more elements left
         while i < len(left):
             arr[k] = left[i]
             i += 1
             k += 1
         while j < len(right):
             arr[k] = right[j]
             j += 1
             k += 1
        
    
def main():
    arr = [3, 5, 2, 7, 1]
    MergeSort(arr)
    print(arr)
    
    
if __name__ == "__main__":
    main()