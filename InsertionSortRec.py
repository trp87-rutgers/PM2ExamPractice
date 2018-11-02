# -*- coding: utf-8 -*-
"""
Tim Petersen
10/31/18
Insertion Sort Recursively
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1), Its for temp
Stability: Yes
"""

def InsertionSortRec(arr, n):
    if n <= 1:
        return
    InsertionSortRec(arr, n-1)
    # above puts the max at end of the list recursively
    temp = arr[n-1] 
    i = n-2
    
    while i>=0 and arr[i]>temp:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = temp
    
def main():
    arr = [5, 8, 7, 1, 2, 6, 9, 0, 10, 4]
    InsertionSortRec(arr, len(arr))
    print(arr)
    
if __name__=="__main__":
    main()
    
"""
Difference between recursive and not is in non every time see n
put n-1 and change the for loop to a function call
"""