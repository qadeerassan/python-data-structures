"""
-------------------------------------------------------
deque_linked.py
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-07-08"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _DequeNode:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _dequeNode(value, prev, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            _prev - another deque node (_DequeNode)
            _next - another deque node (_DequeNode)
        Postconditions:
            Initializes a deque node that contains a copy of value
            and links to the previous and next nodes in the deque.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._prev = _prev
        self._next = _next
        return


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty deque.
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = d.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(d)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the deque.
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: d.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the front of the deque.
        -------------------------------------------------------
        """
        temp = self._front
        node = _DequeNode(deepcopy(value), None, temp)
        self._front = node
        self._count += 1
        if self._rear is None:
            self._rear = node
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: d.insert_rear(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the rear of the deque.
        -------------------------------------------------------
        """
        temp = self._rear
        node = _DequeNode(deepcopy(value), temp, None)
        self._rear = node
        self._count += 1
        if self._front is None:
            self._front = node
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = d.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the front of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty dequeue"

        value = deepcopy(self._front._data)
        self._front = self._front._next
        if self._front is None:
            self._rear = None
        self._count -= 1  

        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = d.remove_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the rear of deque - the value is
                removed from deque.
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty dequeue"

        value = deepcopy(self._rear._data)
        self._rear = self._rear._prev
        if self._rear is None:
            self._front = None      
        self._count -= 1  
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = d.peek_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the front of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty dequeue"

        value = deepcopy(self._front._data)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = d.peek_rear()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the rear of deque -
                the value is not removed from deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty dequeue"

        value = deepcopy(self._rear._data)
        
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Preconditions:
            l - a pointer to a deque node (_DequeNode)
            r - a pointer to a deque node (_DequeNode)
        Postconditions:
            l has taken the place of r, r has taken the place of l and
            _front and _rear are updated as appropriate
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
# 
#         lp = l._prev
#         ln = l._next
#         rp = r._prev
#         rn = r._next
#         
#         if self._front is l:
#             self._front = r
#         if self._rear is l:
#             self._rear = r
#         if self._front is r:
#             self._front = l
#         if self._rear is r:
#             self._rear = l
#             
#         if lp is not None:
#             lp._next = r
#         if rp is not None:
#             rp._next = l
#         if ln is not None:
#             ln._prev = r
#         if rn is not None:
#             rn._prev = l
#             
#         l._next = rn
#         l._prev = rp
#         r._next = ln
#         r._prev = lp

        # Create temporary l
        temp = _DequeNode(l._data, l._prev, l._next)

        # Change l's location
        if r._next is None:
            r._prev._next = l
            self._rear = l
            l._prev = r._prev
            l._next = None

        elif r._prev is None:
            r._next._prev = l
            self._front = l
            l._prev = None
            l._next = r._next

        else:
            r._prev._next = l
            r._next._prev = l
            l._prev = r._prev
            l._next = r._next

        # Change r's location
        if temp._next is None:
            temp._prev._next = r
            self._rear = r
            r._prev = temp._prev
            r._next = None

        elif temp._prev is None:
            temp._next._prev = r
            self._front = r
            r._prev = None
            r._next = temp._next

        else:
            temp._prev._next = r
            temp._next._prev = r
            r._prev = temp._prev
            r._next = temp._next

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the dequeue
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the dequeue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next