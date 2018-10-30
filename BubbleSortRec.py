# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Bubble Sort Recursively
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
Stability: Yes
"""

def BubbleSortRec(arr):
    for i, num in enumerate(arr):
        try: # for list index out of range error
            if arr[i+1] < num:
                # below is basically a swap
                arr[i] = arr[i+1] # element = next element
                arr[i+1] = num # next element = element
                BubbleSortRec(arr) # Recursion
        except: # Index Error but gonna do anything anyway
            pass # keep going anyway

def main():
    arr = [5, 8, 1, 4, 7, 6, 0, 2, 11, 17, 3]
    BubbleSortRec(arr)
    print(arr)

if __name__ == "__main__":
    main()