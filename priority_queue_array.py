"""
-------------------------------------------------------
priority_queue_array.py
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from copy import deepcopy


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
        self._values = []
        self._first = None
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

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
        self._values.append(deepcopy(value))
        n = len(self._values)
        
        if n == 1:
            self._first = 0
        elif self._values[self._first] > value:
            self._first = n - 1
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
        assert len(
            self._values) > 0, "Cannot remove from an empty priority queue"
 
        value = self._values.pop(self._first)
        if len(self._values) > 0:
            self._first = 0
            for i in range(1,len(self._values)):
                if self._values[i] < self._values[self._first]:
                    self._first = i
        else:
            self._first = None
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
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"
        
        value = deepcopy(self._values[self._first])

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
        pq2 = PriorityQueue()
        pq3 = PriorityQueue()
        while len(self._values) > 0:
            if self._values[0] < key:
                pq2._values.append(self._values.pop(0))
            elif len(self._values) > 0 and self._values[0] >= key:
                pq3._values.append(self._values.pop(0))
        return pq2, pq3

    def combine(self, pq2):
        """
        -------------------------------------------------------
        Combines contents of two priority queues into a new 
        priority queue.
        Use: pq3 = pq1.combine(pq2)
        -------------------------------------------------------
        Preconditions:
            q2 - an array-based queue (Queue)
        Postconditions:
            returns
            pq3 - Contents of self and q2 are interlaced 
                into pq3 (Queue)
        -------------------------------------------------------
        """
        pq3 = PriorityQueue()
        while len(self._values) > 0 or len(pq2) > 0:
            if len(self._values) > 0:
                pq3.insert(self._values.pop())
            if len(pq2) > 0:
                pq3.insert(pq2.remove())
        return pq3

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def intersection(self, pq2):
        """
        -------------------------------------------------------
        Returns a queue that contains a set of values that appear only in both q1 and q2.
        Use: pq3 = pq1.intersection(pq2)
        -------------------------------------------------------
        Preconditions:
            pq2 - another queue (Queue)
        Postconditions:
            returns
            pq3 - a new queue that contains only the values found in both q1
            and s2. Values do not repeat. q1 and q2 are empty. (Queue)
        -------------------------------------------------------
        """
        pq3 = PriorityQueue()
        for i in self._values:
            for v in pq2:
                if i == v:
                    pq3.insert(i)
        return pq3
    
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: clean(l)
        -------------------------------------------------------
        Postconditions:
            The list l contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        temp = []
        n = len(self._values)

        while not self._values == 0:
            v = self._values.pop()
            if v not in temp:
                temp.append(v)
        while not len(temp) == 0:
            item = temp.pop()
            self._values.append(item)
            if item < self._first:
                self._first = n-1
        return