"""
An assortment of data structures implimented in Python 3.
"""


def swap(container, i, j):
    container[i], container[j] = container[j], container[i]


class MinimumHeap():
    def __init__(self):
        self.data = [None for _ in range(10)]
        self.data_count = 0

    def _double_array(self):
        self.data = [*self.data, *(None for _ in range(10))]

    def _sink(self, index):
        while index * 2 <= self.data_count:
            max_child_index = index * 2
            
            if max_child_index < self.data_count and self.data[max_child_index] > self.data[max_child_index + 1]:
                max_child_index += 1

            if self.data[index] < self.data[max_child_index]:
                break

            swap(self.data, index, max_child_index)

            index = max_child_index

    def _swim(self, index):
        while index > 1 and self.data[index // 2] > self.data[index]:
            swap(self.data, index, index // 2)
            
            index //= 2

    def insert(self, value):
        self.data_count += 1

        if self.data_count >= len(self.data):
            self._double_array()

        self.data[self.data_count] = value
        
        self._swim(self.data_count)

    def del_min(self):
        maximum_value = self.data[1]

        swap(self.data, 1, self.data_count)

        self.data[self.data_count] = None
        
        self.data_count -= 1
        
        self._sink(1)

        return maximum_value


class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack():
    """
    Implimentation of a FILO (LIFO) structure.
    """
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        new_node.next_node = self.head

        self.head = new_node

    def remove(self):
        tmp_node = self.head

        if tmp_node is not None:
            self.head = tmp_node.next_node 
        else:
            return None

        return tmp_node.value


class Queue():
    """
    Implimentation of a FIFO (LILO) structure.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)

        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def remove(self):
        if self.head is None:
            return None

        tmp_node = self.head

        self.head = tmp_node.next_node

        return tmp_node.value


if __name__ == "__main__":
    from random import shuffle
    
    test_values = [9, 4, 20, 1, 15, 7, 2]

    shuffle(test_values)

    print("Test values:", test_values)

    # Test MinimumHeap
    my_min_heap = MinimumHeap()

    for x in test_values:
        my_min_heap.insert(x)

    print("Min Heap Contents:", my_min_heap.data)

    assert my_min_heap.data_count == len(test_values)
    assert my_min_heap.del_min() == min(test_values)

    # Test Stack
    my_stack = Stack()

    for x in test_values:
        my_stack.add(x)

    for y in reversed(test_values):
        assert my_stack.remove() == y

    # Test Queue
    my_queue = Queue()

    for x in test_values:
        my_queue.add(x)

    for y in test_values:
        assert my_queue.remove () == y
