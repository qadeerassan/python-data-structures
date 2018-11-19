"""
-------------------------------------------------------
bst_linked.py
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2017-08-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from queue_array import Queue

class _BSTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _BSTNode(value)
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes a BST node containing value. Child pointers are None,
            height is 1.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Postconditions:
            _height is 1 plus the maximum of the node's (up to) two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._data)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty bst.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - data to be inserted into the bst (?)
        Postconditions:
            returns
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _data into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - a bst node (_BSTNode)
            value - data to be inserted into the node (?)
        Postconditions:
            returns
            node - the current node (_BSTNode)
            inserted - True if value is inserted into the BST,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BSTNode(value)
            self._count += 1
            inserted = True
        elif node._data > value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._data < value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot retrieve from an empty BST"

        node = self._root
        value = None

        while node is not None and value is None:

            if node._data > key:
                node = node._left
            elif node._data < key:
                node = node._right
            elif node._data == key:
                # for comparison counting
                value = deepcopy(node._data)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns
            value - value matching key if found,
            otherwise returns None. Update structure of bst as required.
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot remove from an empty BST"

        self._root, value = self._remove_aux(self._root, key)
        return value
# 
#     def _remove_aux(self, node, key):
#         """
#         -------------------------------------------------------
#         Attempts to find a value matching key in a BST node. Deletes the node
#         if found and returns the sub-tree root.
#         Private recursive operation called only by remove.
#         Use: node, value = self._remove_aux(node, key)
#         -------------------------------------------------------
#         Preconditions:
#             node - a bst node to search for key (_BSTNode)
#             key - data to search for (?)
#         Postconditions:
#             returns
#             node - the current node or its replacement (_BSTNode)
#             value - value in node containing key, None otherwise.
#         -------------------------------------------------------
#         """
#         if node is None:
#             # Base Case: the key is not in the tree.
#             value = None
#         elif key < node._data:
#             # Search the left subtree.
#             node._left, value = self._remove_aux(node._left, key)
#         elif key > node._data:
#             # Search the right subtree.
#             node._right, value = self._remove_aux(node._right, key)
#         else:
#             # Value has been found.
#             value = node._data
#             # Replace this node with another node.
#             if node._left is None:
#                 # node has no left child or has no children.
# 
# # your code here
# 
# #             elif node._right is None:
#                 # node has no right child.
# 
# # your code here
# 
#             else:
#                 # Node has two children
#                 if node._left._right is None:
#                     # left child is replacement node
#                     repl_node = node._left
#                 else:
#                     # find replacement node in right subtree of left node
#                     repl_node = self._delete_node_left(
#                         node._left, node._left._right)
#                     repl_node._left = node._left
# 
#                 repl_node._right = node._right
#                 node = repl_node
#                 node._update_height()
# 
#             self._count -= 1
# 
#         if node is not None and value is not None:
#             # If the value was found, update the ancestor heights.
#             node._update_height()
#         return node, value

    def _delete_node_left(self, parent, child):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
            child - the right node of parent (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """

        repl_node = self._root
        # Recursively update all parent node heights
        parent._update_height()
        return repl_node
    
    def balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.balanced()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        is_balanced = self._balanced_aux(self._root, True)
        return is_balanced
    
    def _balanced_aux(self, node, is_balanced):
        if is_balanced and node is not None:
            if node._left is not None and node._right is not None:
                if node._left._height == node._right._height:
                    is_balanced = self._balanced_aux(node._left, is_balanced)
                    if is_balanced:
                        is_balanced = self._balanced_aux(node._right, is_balanced)
                else:
                    is_balanced = False
            else:
                is_balanced = False
        return is_balanced
        

    def valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.valid()
        ---------------------------------------------------------
        Postconditions:
            returns
            is_valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        is_valid = self._valid_aux(self._root, True)
        
        return is_valid

    def _valid_aux(self, node, is_valid):
        if is_valid and node is not None:
            is_valid = True
            if node._left is not None:
                if node._data > node._left._data:
                    is_valid = self._valid_aux(node._left, is_valid)
                else:
                    is_valid = False
            if node._right is not None:
                if node._data < node._left._data:
                    is_valid = self._valid_aux(node._right, is_valid)
                else:
                    is_valid = False

        return is_valid
    
    def identical(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.identical(rs)
        -------------------------------------------------------
        Preconditions:
            rs - another bst (BST)
        Postconditions:
            returns
            is_identical - True if this bst contains the same values
            in the same order as rs, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        is_identical = self._identical_aux(self._root, rs._root)

        return is_identical
        
    def _identical_aux(self, node, rs_node):
        is_identical = True
        if is_identical and node is not None and rs_node is not None and node._data == rs_node._data:
            if node._left is not None and rs_node._left is not None:
                is_identical = self._identical_aux(node._left, rs_node._left)
            if is_identical and node._right is not None or rs_node._right is not None:
                is_identical = self._identical_aux(node._right, rs_node._right)
        else:
            is_identical = False

        return is_identical
        
    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Postconditions:
            returns
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero = 0
        one = 0
        two = 0
        zero, one, two = self._node_counts_aux(self._root, zero, one, two)
        return zero, one, two
        
    def _node_counts_aux(self, node, zero, one, two):
        if node is not None:
            if node._left is not None and node._right is not None:
                two += 1
            elif node._left is not None or node._right is not None:
                one += 1
            elif node._left is None and node._right is None:
                zero += 1
            if node._left is not None:
                zero, one, two = self._node_counts_aux(node._left, zero, one, two)
            if node._right is not None:
                zero, one, two = self._node_counts_aux(node._right, zero, one, two)
        
        return zero, one, two
    
    def inorder(self):
        l = []
        l = self._inorder_aux(self._root, l)
        return l
    
    def _inorder_aux(self,node, l):
        if node is not None:
            self._inorder_aux(node._left, l)
            l.append(node._data)
            self._inorder_aux(node._right, l)
        return l

    def preorder(self):
        l = []
        l = self._preorder_aux(self._root, l)
        return l
    
    def _preorder_aux(self,node, l):
        if node is not None:
            l.append(node._data)
            self._inorder_aux(node._left, list)
            self._inorder_aux(node._right, list)
        return list
    
    def postorder(self):
        l = []
        l = self._inorder_aux(self._root, l)
        return
    
    def _postorder_aux(self,node,l):
        if node is not None:
            self._inorder_aux(node._left,l)
            self._inorder_aux(node._right,l)
            l.append(node._data)
        return
    
    def levelorder(self):
        l=[]
        l=self._levelorder_aux(self._root,l)
        return
    
    def _levelorder_aux(self,node,l):
        values = []

        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                values.append(deepcopy(node._data))

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
        return values
            
        return
    
    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        value = self._max_r_aux(self._root)
        
        return value
    
    def _max_r_aux(self, node):
        if node._right is not None:
            value = self._max_r_aux(node._right)
        else:
            value = node._data
        return value
    
    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        value = self._min_aux(self._root)

        return value
    
    def _min_aux(self, node):
        if node._left is not None:
            value = self._min_aux(node._left)
        else:
            value = node._data
        return value
    
    def __iter__(self):
        """
    -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
    -------------------------------------------------------
        Postconditions:
            yields
            value - the values in the BST node and its children (?)
    -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)
    
            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._data
    
                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)

    def count_apply(self, func):
        """
        ---------------------------------------------------------
        Returns the number of values in a BST where func(value) is True.
        Use: number = bst.count_apply(func)
        -------------------------------------------------------
        Preconditions:
            func - a function that given a value in the bst returns
                True for some condition, otherwise returns False.
        Postconditions:
            returns
            number - count of nodes in tree where func(value) is True (int)
        ----------------------------------------------------------
        """
        number = self._count_apply_aux(func, self._root, 0)
        return number
    def _count_apply_aux(self, func, node, number):
        if func(node._data):
            number += 1
        if node._left is not None:
            number = self._count_apply_aux(func, node._left, number)
        if node._right is not None:
            number = self._count_apply_aux(func, node._right, number)
        return number