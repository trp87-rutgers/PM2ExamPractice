# -*- coding: utf-8 -*-
"""
Tim Petersen
10/30/18
Insertion Sort
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complexity: O(1), Its for num
Stability: Yes
"""

def InsertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1 # This is where i will swap with eventually
        
        while j>=0 and temp < arr[j]: # item before is greater than
            arr[j+1] = arr[j]
            j -= 1 # decrement
        arr[j+1] = temp
        
def main():
    arr = [5, 3, 8, 12, 1, 9]
    InsertionSort(arr)
    print(arr)
    
if __name__ == "__main__":
    main()