# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Bubble Sort
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1)
Stability: Yes
"""

def BubbleSort(arr):
    """
        Goes through the array and swaps adjacent items
        If goes through array and does not swaps it stops
    """
    while True: # Do till sorted
        swapped = False
        for j in range(len(arr)-1): # go through list except last
            if arr[j] > arr[j+1]: # if next item is greater than item
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
                swapped = True # we swapped possible more swaps to do
        if swapped == False: # didnt swap on iteration of for so break
            break
    
def main():
    arr = [2, 8, 1, 6, 9, 12, 0, 5]
    BubbleSort(arr)
    print(arr)
    
if __name__ == "__main__":
    main()