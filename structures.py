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


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack():
    """
    Implimentation of a FILO (LIFO) structure.
    """
    def __init__(self):
        self.head = None

    def __len__(self):
        tmp_node = self.head
        count = 0

        while tmp_node is not None:
            tmp_node = tmp_node.next_node
            count += 1

        return count

    def push(self, value):
        new_node = LinkedListNode(value)
        new_node.next_node = self.head

        self.head = new_node

    def pop(self):
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

    def enqueue(self, value):
        new_node = LinkedListNode(value)

        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        tmp_node = self.head

        self.head = tmp_node.next_node

        return tmp_node.value


class StackQueue():
    """
    An implimentation of a queue using two stacks.
    
    Note: Never do this in the real world! :)
    """
    def __init__(self):
        self.in_stack, self.out_stack = Stack(), Stack()

    def enqueue(self, value):
        self.in_stack.push(value)

    def dequeue(self):
        if not len(self.out_stack):
            while len(self.in_stack):
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()


class BinaryTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def put(self, value):
        def _put(node, node_value):
            if node is None:
                return BinaryTreeNode(node_value)

            if value < node.value:
                node.left = _put(node.left, node_value)
            elif value > node.value:
                node.right = _put(node.right, node_value)
            else:
                node.value = node_value

            return node

        self.root = _put(self.root, value)

    def get(self, value):
        """
        This method is just a modification of binary search.
        Rather than moving the left and right indexes of the
        container, we move left or right in the tree, essentially
        obtaining the same goal.
        """
        tmp_node = self.root

        while tmp_node is not None:
            if tmp_node.value < value:
                tmp_node = tmp_node.left
            elif tmp_node.value > value:
                tmp_node = tmp_node.right
            else:
                return tmp_node.value
        else:
            return None

    def rotate_left(self, node):
        right_node = node.right

        node.right = right_node.left

        right_node.left = node

        return right_node

    def rotate_right(self, node):
        """ Just swap the words "left" and "right" :) """
        left_node = node.left

        node.left = left_node.right

        left_node.right = node

        return left_node


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
        my_stack.push(x)

    for y in reversed(test_values):
        assert my_stack.pop() == y

    # Test Queue
    my_queue = Queue()

    for x in test_values:
        my_queue.enqueue(x)

    for y in test_values:
        assert my_queue.dequeue() == y

    # Test StackQueue
    my_stack_queue = StackQueue()

    for x in test_values:
        my_stack_queue.enqueue(x)

    for y in test_values:
        assert my_stack_queue.dequeue() == y
