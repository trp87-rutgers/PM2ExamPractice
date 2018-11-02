# -*- coding: utf-8 -*-
"""
Tim Petersen
11/1/18
Binary Search
Best Case: O(1)
Average Case: O(logn)
Worst Case: O(logn)
Space Complexity: O(1)
"""

from Mergesort import MergeSort

def BinarySearch(arr, num, lo, hi):
    while hi-lo>=0:
        mid = (hi+lo)//2
        if num == arr[mid]:
            return mid
        if num > arr[mid]:
            lo = mid+1
        if num < arr[mid]:
            hi = mid-1

def main():
    arr = [3, 6, 1, 8, 9, 0, 2, 7]
    #arr = [3, 1, 5]
    MergeSort(arr)
    print(arr)
    index = BinarySearch(arr, 3, 0, len(arr)-1)
    print(index)
    

if __name__ == "__main__":
    main()