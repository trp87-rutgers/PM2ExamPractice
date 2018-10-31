# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Merge Sort
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(n)
Stability: Yes
"""


def Merge(arr, lo, m, hi):
    # eventual lengths of the two arrays
    len1 = m-lo
    len2 = hi-m
    
    
    # Create temporaty arrays that are a copy of the split arrs
    temp1 = arr[lo:m]
    temp2 = arr[m:hi]
    
    i = 0 # temp1 index
    j = 0 # temp2 index
    k = lo # arr index
    
    # put two temp arrays in order into final array
    while i<len1 and j<len2:
        if temp1[i]<temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1
        
    # must deal with remaining elements if any
    while i<len1:
        arr[k] = temp1[i]
        i += 1
        k += 1
        
    while j<len2:
        arr[k] = temp2[j]
        j += 1
        k += 1
    print(arr)
    
    
    
def MergeSort(arr, lo, hi):
    if hi > lo:
         m = (lo+hi-1)//2 # int division cause if its odd
         print(lo, m, hi)
         MergeSort(arr, lo, m)
         MergeSort(arr, m+1, hi)
         print(arr)
         Merge(arr, lo, m, hi)
    
def main():
    arr = [3, 5, 2, 7, 65, 10, 2, 1, 0]
    #n = len(arr)
    #m = n//2
    #print(m, n)
    #temp1 = [0] * (m-0)
    #temp2 = [0] * (n-m)
    #temp1 = arr[0:m]
    #temp2 = arr[m:n]
    #print(temp1)
    #print(temp2)
    MergeSort(arr, 0, len(arr)-1)
    print(arr)
    
    
if __name__ == "__main__":
    main()