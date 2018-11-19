"""
-------------------------------------------------------
queue_array.py
Array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from copy import deepcopy
from stack_array import Stack

class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty queue.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = q.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = q.is_full()
        -------------------------------------------------------
        Postconditions:
            Returns True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(q)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: q.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the queue.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = q.remove()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of the queue - the value is
            removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        value = self._values.pop(0)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = q.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of the queue -
            the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])
        return value

    def combine(self, q2):
        """
        -------------------------------------------------------
        Combines contents of two queues into a new queue.
        Use: q3 = q1andq2.combine(q2)
        -------------------------------------------------------
        Preconditions:
            q2 - an array-based queue (Queue)
        Postconditions:
            returns
            q3 - Contents of self and q2 are interlaced 
                into q3 (Queue)
        -------------------------------------------------------
        """

        # your code here

        return q3

    def split(self):
        """
        -------------------------------------------------------
        Splits a queue into two other queues with values 
        alternating between target queues.
        Use: q2, q3 = q1andq2.split()
        -------------------------------------------------------
        Postconditions:
            returns
            q2 - a target (Queue)
            q3 - a second target (Queue)
            Contents of the current queue are moved alternately 
            to q2 and q3. Current queue is empty.
        -------------------------------------------------------
        """
 
        # your code here

        return q2, q3
    
    def identical(self, q2):
        """
        ----------------
        Determines whether two given queues are identical.
        Entries of q1andq2 and q2 are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: b = q1andq2.identical(q2)
        ---------------
        Preconditions:
            q2 - a queue object (Queue)
        Postconditions:
            returns
            is_identical - True if q1andq2 and q2 are identical, False otherwise. 
                Queues are unchanged. (boolean)
        ---------------
        """
        q1_a = []
        while len(self._values) > 0:
            q1_a.insert(0,self._values.pop())
        q2_a = []
        while q2.is_empty() != True:
            q2_a.insert(0,q2._values.pop())
        if q1_a == q2_a:
            is_identical = True
        else:
            is_identical = False
        for _ in range(len(q1_a)):
            value = q1_a.pop(0)
            self._values.append(value)
        for _ in range(len(q2_a)):
            value = q2_a.pop(0)
            q2.insert(value)
        return is_identical
    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
 
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in a queue.
        Use: q.reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of q are reversed in order with respect
            to their order before the operation was called.
        -------------------------------------------------------
        """
        s = Stack()
        print('use')
        while len(self._values) > 0:
            v = self._values.pop(0)
            s.push(v)
        while not s.is_empty():
            self._values.append(s.pop())
        return
        
    def intersection(self, q2):
        """
        -------------------------------------------------------
        Returns a queue that contains a set of values that appear only in both q1 and q2.
        Use: q3 = q1.intersection(q2)
        -------------------------------------------------------
        Preconditions:
            q2 - another queue (Queue)
        Postconditions:
            returns
            q3 - a new queue that contains only the values found in both q1
            and q2. Values do not repeat. q1 and q2 are empty. (Queue)
        -------------------------------------------------------
        """
        q3 = Queue()
        for i in self._values:
            for v in q2:
                if i == v and i:
                    q3.insert(i)
        return q3      
    
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list.
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        temp = []
        while not len(self._values) == 0:
            v = self._values.pop()
            if v not in temp:
                temp.append(v)
        while not len(temp) == 0:
            self._values.append(temp.pop())
        
    
    