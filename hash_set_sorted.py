"""
-------------------------------------------------------
hash_set_array.py
Array version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-11-14"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from sorted_list_linked import SortedList
# Define the new_slot slot creation function.

# Constants
SEP = '-' * 40


class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Precondition:
            slots - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._total = int(self._slots * self._LOAD_FACTOR)

        for _ in range(self._slots):
            self._table.append(SortedList())
            
        self._count = 0
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
    
    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        hashkey = hash(key) % self._slots
        slot = self._table[hashkey]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot
    
    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
        Calls _rehash if the hashset _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        hash_slot = self._find_slot(value)
        
        if value not in hash_slot:
            hash_slot.insert(value)
            inserted = True
            self._count += 1
        else:
            inserted = False
            
        if self._count > self._total:
            self._rehash()

        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        hash_slot = self._find_slot(key)
        assert len(hash_slot) > 0, "Cannot remove from empty slot."
        
        if key in hash_slot:
            index = hash_slot.index(key)
            value = hash_slot.remove(index)
            self._count -= 1
        else:
            value = None
            
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates the
        existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """
        slots = self._slots * 2 + 1
        add_slots = slots - self._slots
        for _ in range(add_slots):
            self._table.append(SortedList())
            self._slots += 1

        for slot in self._table:
            for key in slot:
                new_slot = self._find_slot(key)
                new_slot.insert(key)
                index = slot.index(key)
                slot.pop(index)
        self._total = self._LOAD_FACTOR * self._slots
        
        return

    def debug(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed and the slots identified.
        -------------------------------------------------------
        """
        for slot in range(len(self._table)):
            print("Slot {}".format(slot))
            print()
            for key in self._table[slot]:
                print(key)
                print()
        return

    def print_i(self):

        for slot in self._table:
            slot.print_i()
        return
    
    def __iter__(self):
        for slot in self._table:
            for value in slot:
                yield value
        
        