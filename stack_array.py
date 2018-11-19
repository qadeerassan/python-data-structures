"""
-------------------------------------------------------
stack_array.py
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-08-19"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """
        b = False
        if len(self._values) == 0:
            b = True
        
        return b

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the value at the top of the stack - the value is
                removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        
        value = self._values.pop()
        
        return value
        
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the top of the stack -
                the value is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = deepcopy(self._values[-1])

        return value
 
    def combine(self, s2):
        """
        -------------------------------------------------------
        Combines a second stack with the current stack.
        (iterative algorithm)
        Use: s3 = s1.combine(s2)
        -------------------------------------------------------
        Preconditions:
            s2 - an array-based stack (Stack)
        Postconditions:
            Returns:
            s3 - the contents of the current stack and s2
                are interlaced into s3 - current stack and s2
                are empty (Stack)
        -------------------------------------------------------
        """
        s3 = Stack()
        while len(self._values) > 0 or len(s2._values) > 0:
            if len(self._values) > 0 == False:
                s3._values.append(self._values.pop())
            if len(s2._values) > 0 == False:
                s3._values.append(s2._values.pop())
        return s3

    def split(self):
        """
        -------------------------------------------------------
        Splits the current stack into separate stacks. Current stack is empty
        when operation is done.
        Use: s2, s3 = s1.split()
        -------------------------------------------------------
        Postconditions:
            returns
            s2 - contains alternating values from current stack (Stack)
            s3 - contains other alternating values from current stack (Stack)
        -------------------------------------------------------
        """
        s2 = Stack()
        s3 = Stack()
        
        while len(self._values) > 0 != True:
            s2._values.append(self._values.pop())
            if len(self._values) > 0 != True:
                s3._values.append(self._values.pop())
        return s2, s3

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            returns
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
            
    def intersection(self, s2):
        """
        -------------------------------------------------------
        Returns a queue that contains a set of values that appear only in both q1 and q2.
        Use: s3 = s1.intersection(s2)
        -------------------------------------------------------
        Preconditions:
            s2 - another queue (Queue)
        Postconditions:
            returns
            s3 - a new queue that contains only the values found in both q1
            and s2. Values do not repeat. q1 and q2 are empty. (Queue)
        -------------------------------------------------------
        """
        s3 = Stack()
        for i in self._values:
            for v in s2:
                if i == v and i not in s3:
                    s3.push(i)
        return s3
    
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
        