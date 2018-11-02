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

class MinHeap:
    def __init__(self):
        self.list = []
    def add(self, a):
        self.list.append(a)
        if len(self.list) > 1:
            self.swim(len(self.list)-1) # sends position of added item
        
    def getParent(self, a):
        """
        Takes in a position argument returns parent position
        """
        return a//2
    
    def getKid(self, a, pos=0):
        """
        Takes in position of parent and which child as True or False
        0 for first kid
        1 for second kid
        If no pos argument is given then first kid is returned
        """
        return (2*a+pos)
    
    def swap(self, a, b):
        self.list[a], self.list[b] = self.list[b], self.list[a]
    
    def swim(self, a): # a is position
        while self.list[a] < self.list[self.getParent(a)]:
            self.swap(a, self.getParent(a))
            a = self.getParent(a)
            
    def prnt(self):
        for num in self.list:
            print(num)
                    
    def sink(self, pos):
        if pos > len(self.list):
            return
        val = self.list[pos]
        kid1 = self.getKid(pos)
        kid2 = self.getKid(pos, 1)
        val1 = val if kid1 > len(self.list)-1 else self.list[kid1]
        val2 = val if kid2 > len(self.list)-1 else self.list[kid2]
        swapKid = None
        if val1 <= val2 and val1< val:
            swapKid = kid1
        elif val2 < val1 and val2 < val:
            swapKid = kid2
        if swapKid is None:
            return
        self.swap(pos, swapKid)
        self.sink(swapKid)
            
    def delMin(self):
        if len(self.list) > 1:
            self.list[0] = self.list[len(self.list)-1]
            self.list.pop(len(self.list)-1)
            self.sink(0)
        else:
            self.list = []
    
    def heapify(self, arr):
        """
            All leaves at bottom of list are a heap individually so go 
            backwards and work your way up to make a valid heap one by one on
            all the parent nodes
            Runs in O(n) b/c math - sink is not run on bottom leaves, and sink
            is only run once on parent of bottom leaves. Add all of it up going 
            to the root node with math and get n
        """
        self.list = arr[:]
        for i in range(len(self.list)-1, -1, -1):
            self.sink(i)

            
def main():
    heap = MinHeap()
    heap.add(8)
    heap.add(4)
    heap.add(10)
    heap.add(2)
    heap.add(9)
    heap.add(3)
    heap.prnt()
    print()
    heap.delMin()
    heap.prnt()
    arr = [5, 3, 8, 0, 10, 2, 7]
    h2 = MinHeap()
    h2.heapify(arr)
    print()
    h2.prnt()
    
if __name__ == "__main__":
    main()
            