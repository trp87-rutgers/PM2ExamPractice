# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:45:05 2018

@author: Tim
"""

# import statements
from collections import deque # double ended queue

q = deque()
q.append(3) # appends like usual
q.appendleft(2) # appends to front of list
q.count(3) # returns how many times 3 is in the queue
q.extend([3, 5, 8]) # appends multiple things on queue
q.extendleft([8,4, 3]) # appends multiple things to front of queue
q.pop() # removes last item in queue
q.popleft() # removes first item in queue

# Min heap
import heapq # offers heapifu heappush and heappop
#acts as a class of functions
lst = [5, 4, 8, 1, 3, 6, 0, 9]
heapq.heapify(lst)
print(lst)
heapq.heappush(lst, 2)
heapq.heappop(lst)
heapq.heapreplace(lst, 4)



#Quues are already built in
size = 4
 q1 = queue.Queue(size)
queue.put(5)
queue.get(0) # 0 refers to the element
q1.full() # returns boolean