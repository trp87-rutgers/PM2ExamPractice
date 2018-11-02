# -*- coding: utf-8 -*-
"""
Tim Petersen
11/1/18
Binary Search Tree


"""

class Node:
    def __init__(self, val):
        self.val = val
        self.R = None
        self.L = None

class BST:
    def __init__(self):
        self.root = None
        
    def add(self, a):
        node = Node(a)
        if self.root == None:
            self.root = node
        else:
            tempNode = self.root
            while tempNode is not None:
                if a > tempNode.val:
                    if tempNode.R == None:
                        break
                    else:
                        tempNode = tempNode.R
                elif a < tempNode.val:
                    if tempNode.L == None:
                        break
                    else:
                        tempNode = tempNode.L
                else: return
            if a > tempNode.val:
                tempNode.R = node
            else:
                tempNode.L = node
    
    def search(self, num):
        if self.root == None:
            return False
        else:
            tempnode = self.root
            while tempnode is not None:
                if num > tempnode.val:
                    if tempnode.R == None:
                        return False
                    else:
                        tempnode = tempnode.R
                elif num < tempnode.val:
                    if tempnode.L == None:
                        return False
                    else:
                        tempnode = tempnode.L
                else:
                    return True
            
    def delete(self, num):
        tempnode = self.root
        while tempnode is not None:
            if num > tempnode.val:
                if tempnode.R == None:
                    return
                else:
                    tempnode = tempnode.R
            elif num < tempnode.val:
                if tempnode.L == None:
                    return
                else:
                    tempnode = tempnode.L
            else: # found the number
                    
    

def main():
    bst = BST()
    bst.add(3)
    bst.add(2)
    bst.add(5)
    print(bst.root.R.val)
    
if __name__ == "__main__":
    main()