"""
-------------------------------------------------------
priority_queue_linked.py
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2018-03-07"
-------------------------------------------------------
"""
from copy import deepcopy


class _PQNode:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node.
        Use: node = _PQNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _next - another priority queue node (_PQNode)
        Postconditions:
            Initializes a priority queue node that contains a copy of value
            and a link to the next node in the priority queue.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = _next
        return


class PriorityQueue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the priority queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the priority queue.
        Use: pq.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the priority queue.
        -------------------------------------------------------
        """
        node = _PQNode(value, None)
        
        if self._front is None:
            self._front = node
        
        elif self._front._data < value:
            self._front = node
        
        current = self._front
        while current._next is not None:
            current = current._next
        current._next = node
        
        self._count += 1
        
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the priority queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the highest priority value in the priority queue -
            the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"
        value = self._front._data
        self._front = self._front._next
        self._count -= 1
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the highest priority value in the priority queue -
            the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        value = deepcopy(self._front._data)
        
        return value

    def split(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The split is stable.
        Use: pq2, pq3 = pq1.split(key)
        -------------------------------------------------------
        Preconditions:
            key - a data object (?)
        Postconditions:
            returns
            pq2 - a priority queue that contains all values
                with priority less than key (PriorityQueue)
            pq3 - priority queue that contains all values with
                priority greater than or equal to key (PriorityQueue)
            The current priority queue is empty
        -------------------------------------------------------
        """
#         current = self._front
#         pq2 = PriorityQueue()
#         pq3 = PriorityQueue()
#         
#         while current is not None:
#             if pq2._front is None and current._data < key:
#                 pq2._front = current
#             elif current._data < key and pq2._front._next is None:
#                 pq2._front._next = current
#             pq2_curr = pq2._front._next
#             if current._data < key:
#                 pq2_curr._next = current
#                 pq2_curr = pq2_curr._next
#             if pq3._front is None and current._data >= key:
#                 pq3._front = current
#             elif current._data >= key and pq3._front._next is None:
#                 pq3._front._next = current
#             pq3_curr = pq3._front._next
#             if current._data >= key:
#                 pq3_curr._next = current
#                 pq3_curr = pq2_curr._next
#             current = current._next
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()

        prev = None
        current = self._front

        # Traverses and finds the location of where the split occurs
        while current is not None and current._data < key:
            prev = current
            current = current._next
            pq3._count += 1
        pq2._front = current
        pq2._count = self._count - pq3._count

        if prev is not None:
            pq3._front = self._front
            prev._next = None

        self._count = 0
        self._front = None

        return pq2, pq3

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next