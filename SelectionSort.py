# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Selection Sort
Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
Stability: No
"""

def Swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    print(arr)

def SelectionSort(arr):
    """
    Process:
        Go through whole array find min
        insert min at position of outer loop
        so go one by one in the array and place the min
    """
    for i in range(len(arr)): # Go through whole array
        minIn = i
        for j in range(i+1, len(arr)): # Find min
            if arr[minIn] > arr[j]:
                minIn = j # got the min
        print(arr)
        Swap(arr, i, minIn)
        
def main():
    arr = [5, 1, 8, 12, 4, 2, 18]
    SelectionSort(arr)
    print(arr)
    
if __name__ == "__main__":
    main()