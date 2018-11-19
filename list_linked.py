"""
-------------------------------------------------------
list_linked.py
Linked version of the list ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""
from copy import deepcopy


class _ListNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            _data - data value for node (?)
            _next - another list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
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
            returns
            True if the list is empty, False otherwise.
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
            returns
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the list at index i.
        Use: l.insert(i, value)
        -------------------------------------------------------
        Preconditions:
            i - index value (int)
            value - a data element (?)
        Postconditions:
            a copy of value is added to index i, all other values are pushed right
            If i outside of range of length of list, appended to end
        -------------------------------------------------------
        """
        if i < 0:
            # negative index
            i = self._count + i

        n = 0
        previous = None
        current = self._front

        while n < i and current is not None:
            # find the proper location in the list
            previous = current
            current = current._next
            n += 1

        if previous is None:
            # Insert a new node into the front of the list.
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            previous._next = _ListNode(value, current)
        self._count += 1
        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        self.insert(0, deepcopy(value))
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
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

    def _linear_search_r_aux(self, previous, current, key):
        i = 0
        if current is not None:
            if current._data != key:
                previous, current, index = self._linear_search_r_aux(current, current._next, key)
                i = 1 + index
        return previous, current, i
    
    def _linear_search_r(self, key):
        previous, current, i = self._linear_search_r_aux(None, self._front, key)
        
        if current is None:
            i = -1
            
        return previous, current, i
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove(key)
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

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._data
        self._front = self._front._next
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        _,_,temp = self._linear_search(key)
        while temp != -1:
            self.pop(temp)
            _,_,temp = self._linear_search(key)

        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        #_,current,_= self._linear_search(key)
        #to save memory, we can use underscores as we need 3 variables for linear_search()
        _,c,_ = self._linear_search(key)
        current = c
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
        value = deepcopy(self._front._data)

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        #,_,_=self._linear_search(key)
        p,c,i = self._linear_search(key)


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

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Preconditions:
            i - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
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

        current._data = deepcopy(value)
        return

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
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
            returns
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        max_data = current._data
        
        while current is not None:
            if current._data > max_data:
                max_data = current._data
            current = current._next 
        max_data = deepcopy(max_data)

        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
            returns
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        min_data = current._data
        
        while current is not None:
            if current._data < min_data:
                min_data = current._data
            current = current._next
        min_data = deepcopy(min_data)

        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        current = self._front
        number = 0
        while current is not None:
#             print(current._data)
            if current._data == key:
                number +=1
      
            current = current._next

        return number

    def append(self, value):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the List.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the List.
        -------------------------------------------------------
        """
        # self.insert(self._count, value)

        previous = None
        current = self._front

        while current is not None:
            previous = current
            current = current._next

        if previous is None:
            self._front = _ListNode(deepcopy(value), self._front)
        else:
            previous._next = _ListNode(deepcopy(value), current)
        self._count += 1

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (iterative algorithm)
        Use: l.clean()
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

    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            is_identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != rs._count:
            is_identical = False
        else:
            current1 = self._front
            current2 = rs._front

            while current1 is not None and current1._data == current2._data:
                current1 = current1._next
                current2 = current2._next

            is_identical = current1 is None
        return is_identical
    
    def identical_r_aux(self, current1, current2):
        if current1 == None:
            is_identical = True
        else:
            if current1._data != current2._data:
                is_identical = False
            else:
                is_identical = self.identical_r_aux(current1._next, current2._next)
        return is_identical
    
    def identical_r(self, rs):
        
        if self._count != rs._count:
            is_identical = False
        else:
            is_identical = self.identical_r_aux(self._front, rs._front)
        return is_identical
    
    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        Use: l.reverse()
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
    
    def reverse_r_aux(self, new_front):
        if self._front is not None:
            temp = self._front._next
            self._front._next = new_front
            new_front = self._front
            self._front = temp
            
            new_front = self.reverse_r_aux(new_front)

        return new_front
    
    def reverse_r(self):        
        new_front = self.reverse_r_aux(None)
        
        self._front = new_front
        return
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant.
        -------------------------------------------------------
        Postconditions:
            returns
            even - the even indexed elements of the list (List)
            odd - the odd indexed elements of the list (List)
            The list is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()

        while self._front is not None:
            new_node = self._front
            self._front = self._front._next
            new_node._next = even._front
            even._front = new_node

            if self._front is not None:
                new_node = self._front
                self._front = self._front._next
                new_node._next = odd._front
                odd._front = new_node

        odd._count = self._count // 2
        even._count = self._count - odd._count
        self._count = 0
        return even, odd
    
    def split_alt_r_even_aux(self, even, odd):
        if self._front is not None:
            new_node = self._front
            self._front = self._front._next
            new_node._next = even._front
            even._front = new_node
            if self._front is not None:
                even, odd = self.split_alt_r_odd_aux(even, odd)
        return even, odd
    
    def split_alt_r_odd_aux(self, even, odd):
        if self._front is not None:
            new_node = self._front
            self._front = self._front._next
            new_node._next = odd._front
            odd._front = new_node
            if self._front is not None:
                even, odd = self.split_alt_r_even_aux(even, odd)
        return even, odd
    
    def split_alt_r(self):
        even = List()
        odd = List()
        
        if self._front is not None:
            even, odd = self.split_alt_r_even_aux(even, odd)
      
        odd._count = self._count // 2
        even._count = self._count - odd._count
        self._count = 0
        even.reverse_r()
        odd.reverse_r()
        return even, odd
    
    def intersection(self, rs):
        """
        -------------------------------------------------------
        Copies only the values common to both the current list and rs
        to a new list.
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains one copy of values common to current list
                and rs (List)
        -------------------------------------------------------
        """
        new_list = List()
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
    
    def intersection_r_check_aux(self, cur_node, next_node):
        if next_node is not None:
            if next_node._data != cur_node._data:
                cur_node, next_node = self.intersection_r_check_aux(
                    cur_node, next_node._next)

        return cur_node, next_node
    
    def intersection_r_aux(self, new_list, cur_self, rs):
        if cur_self is not None:
            _, cur_new_list = self.intersection_r_check_aux(
                cur_self, new_list._front)

            if cur_new_list is None:
                _, cur_rs = self.intersection_r_check_aux(cur_self, rs)

                if cur_rs is not None:
                    new_list.append(cur_self._data)

            self.intersection_r_aux(new_list, cur_self._next, rs)

        return new_list

    def intersection_r(self, rs):
        return self.intersection_r_aux(List(), self._front, rs._front)
        
    def union(self, rs):
        """
        -------------------------------------------------------
        Returns a list that contains all values in both
        the current List and rs. (iterative algorithm)
        Use: nl = l.union(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another list (List)
        Postconditions:
            returns
            new_list - contains all values found in both the current
            List and rs. Values do not repeat. (List)
        -------------------------------------------------------
        """
        new_list = List()
        temp = self._front
        temp2 = rs._front
        
        while temp is not None:
            _,_,in_nL = new_list._linear_search(temp._data)
            if in_nL is -1:
                new_list.append(temp._data)
            temp = temp._next
        while temp2 is not None:
            _,_,in_nL = new_list._linear_search(temp2._data)
            if in_nL is -1:
                new_list.append(temp2._data)
            temp2 = temp2._next
        return new_list
    
    def combine(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(s2)
        -------------------------------------------------------
        Preconditions:
            s2- an linked-based List (List)
        Postconditions:
            returns
            new_list - the contents of the current List and s2
            are interlaced into new_list - current List and s2
            are empty (List)
        -------------------------------------------------------
        """
        new_list = List()
        temp = self._front
        temp2 = rs._front
        
        while temp is not None or temp2 is not None:
            if temp is not None:
                _,_,in_nL = new_list._linear_search(temp._data)
                if in_nL is -1:
                    new_list.append(temp._data)
                temp = temp._next
            if temp2 is not None:
                _,_,in_nL2 = new_list._linear_search(temp2._data)
                if in_nL2 is -1:
                    new_list.append(temp2._data)
                temp2 = temp2._next
        return new_list
    
    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. ls contains the first half,
        rs the second half. Uses counting algorithm.
        Current list is empty.
        Use: ls, rs = l.split_th()
        -------------------------------------------------------
        Postconditions:
            returns
            ls - a new List with >= 50% of the original List (List)
            rs - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        ls = List()
        rs = List()
        half = self._count // 2
        i = 0
        
        while i < self._count and self._front is not None:
            if self._front is not None and i <= half:
                new_node = self._front
                self._front = self._front._next
                new_node._next = ls._front
                ls._front = new_node
            elif self._front is not None and i > half:
                new_node = self._front
                self._front = self._front._next
                new_node._next = rs._front
                rs._front = new_node
            i += 1
        ls.reverse()
        rs.reverse()
        ls._count = self._count // 2
        rs._count = self._count - ls._count
        self._count = 0
        return ls, rs

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
            
    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Preconditions:
            pln - node before list node to swap (_ListNode)
            prn - node before list node to swap (_ListNode)
        Postconditions:
            The nodes in pln.next and prn.next have been swapped,
                and all links to them updated.
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                l = self._front
                self._front = prn._next
            else:
                l = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                r = self._front
                self._front = l
            else:
                r = prn._next
                prn._next = l

            # Swap next pointers
            # l._next, r._next = r._next, l._next
            temp = l._next
            l._next = r._next
            r._next = temp
        return