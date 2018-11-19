"""
-------------------------------------------------------
sorted_list_linked.py
Linked version of the SortedList ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-02-24"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SLNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SLNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            value - data value for node (?)
            next_ - another sorted list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class SortedList:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty sorted list.
        Use: sl = SortedList()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty sorted list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        # Loop through the linked list to find the proper position for _data.
        while current is not None and value >= current._data:
            previous = current
            current = current._next

        # Create the new node and link it to current.
        node = _SLNode(deepcopy(value), current)

        if previous is None:
            # The new node is the first node in the linked list.
            self._front = node
        else:
            # The previous node is linked to the new node.
            previous._next = node

        # Increment the priority queue size.
        self._count += 1

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0
  
        while current is not None and current._data != key:
            previous = current
            current = current._next
            index +=1
        
        if current is None:
            index = -1
        
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
       
        previous, current, index = self._linear_search(key)
        if index == -1:
            value = None
        else: 
            value = current._data
            if previous is None:
                self._front = current._next
                #setting the new front to the next node if the first number is equal o key
            else:
                previous._next = current._next
                #we're removing the node by skipping over the current current data npde
             
            self._count -=1
            
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find in an empty list"
       
        _,current,_ = self._linear_search(key)
        if current is not None:
            value = deepcopy(current._data)
        else:
            value = None

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._data)

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)

        return i

    def _valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._valid_index(i)
        -------------------------------------------------------
        Preconditions:
            i - an index value (int)
        Postconditions:
            returns
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
        Postconditions:
            returns
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._valid_index(i), "Invalid index value"

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._data)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _,current,_ = self._linear_search(key)

        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        value = current._data
        
        while current is not None:
            if current._data > value:
                value = deepcopy(current._data)
            current = current._next 

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        current = self._front
        value = current._data
        
        while current is not None:
            if current._data < value:
                value = deepcopy(current._data)
            current = current._next 

        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            returns
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        current = self._front
        number = 0
        while current is not None:
            if current._data == key:
                number += 1
            current = current._next
            
        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        key_node = self._front

        while key_node is not None:
            # Loop through every node - compare each node with the rest
            previous = key_node
            current = key_node._next

            while current is not None:
                # Always search to the end of the list (may have > 1 duplicate)
                if current._data == key_node._data:
                    # Remove the current node by connecting the node before it
                    # to the node after it.
                    previous._next = current._next
                    self._count -= 1
                else:
                    previous = current
                # Move to the _next node.
                current = current._next
            # Check for duplicates of the _next remaining node in the list
            key_node = key_node._next
        
        return

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Preconditions:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Postconditions:
            returns
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._data

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (SortedList)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()
        temp = rs._front

        while temp is not None:
            _, current, _ = self._linear_search(temp._data)

            if current is not None:
                # Value exists in both lists.
                _, current, _ = new_list._linear_search(temp._data)

                if current is None:
                    # Value does not appear in new list.
                    new_list.insert(0, temp._data)

            temp = temp._next

        return new_list

    def union(self, rs):
        """
        -------------------------------------------------------
        Copies all of the values in both self and rs to
        a new List. Each value appears only once. (iterative)
        -------------------------------------------------------
        Preconditions:
        rs - another List (SortedList)
        Postconditions:
        Returns:
        new_list - a List containing one copy each of all values
        in both self and rs. (SortedList)
        -------------------------------------------------------
        """
        new_list = SortedList()

        temp = self._front
        temp2 = rs._front
        
        while temp is not None:
            _,_,in_nL = new_list._linear_search(temp._data)
            if in_nL is -1:
                new_list.insert(temp._data)
            temp = temp._next
        while temp2 is not None:
            _,_,in_nL = new_list._linear_search(temp2._data)
            if in_nL is -1:
                new_list.insert(temp2._data)
            temp2 = temp2._next
        return new_list

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = sl.remove_front()
        -------------------------------------------------------
        Postconditions:
          Returns:
          value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """
        value = self._front._data
        self._front = self._front._next
        self._count -= 1
        
        return value

    def _reverse(self):
        """
        -------------------------------------------------------
        Helper method - reverses the order of the elements in list.
        Use: l._reverse()
        -------------------------------------------------------
        Postconditions:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next
            
