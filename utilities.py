"""
----------------------------------------------------
utilities.py
Stack utilities.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-12"
----------------------------------------------------
"""
from food import Food
from stack_array import Stack
from queue_array import Queue
from list_array import List
from priority_queue_array import PriorityQueue
from queue_circular import CircularQueue

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of a onto s.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        The contents of a are moved into s, a is empty.
    -------------------------------------------------------
    """
    for _ in range(len(a)):
        val = a.pop(0)
        s.push(val)
    
def stack_to_array(s, a):
    """
    -------------------------------------------------------
    Pops contents of s into a.
    Use: stack_to_array(s, a)
    -------------------------------------------------------
    Preconditions:
        s - a Stack object (Stack)
        a - a Python list (list)
    Postconditions:
        Contents of s are moved into a, s is empty.
    -------------------------------------------------------
    """
    while s.is_empty() != True:
        a.insert(0, s.pop())
    return

def stack_test(a):
    """
    -------------------------------------------------------
    Tests 
    Use: stack_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Stack are tested for both empty and 
        non-empty stacks using the data in a:
        empty, push, pop, peek
    -------------------------------------------------------
    """
    s = Stack()
    print("a: {}".format(a))
    #is_Empty
    print("Tests s.is_Empty: {}".format(s.is_empty()))
    array_to_stack(s, a)
    print("Tests s.is_Empty again: {}".format(s.is_empty()))
    print("Stack after array_to_stacks: ")
    for v in s:
        print(v)
    #push
    print("Pushes '21' to the top of the stack: ")
    s.push(21)
    #pop
    print("Tests pop: {}".format(s.pop()))
    #peek
    print("Tests peek: {}".format(s.peek()))
    
    print("Stack to array: ")
    stack_to_array(s, a)
    print(a)
    return

def array_to_queue(q, a):
    for _ in range(len(a)):
        value = a.pop(0)
        q.insert(value)
    return
    
def queue_to_array(q, a):
    while q.is_empty() != True:
        a.insert(0,q.remove())
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    print("***Is_empty test 1: {}".format(q.is_empty()))
    print("***Array_to_queue ->")
    array_to_queue(q, a)
    print("***Is_empty test 2: {}".format(q.is_empty()))
    print("***Tests remove(): {}".format(q.remove()))
    print("***Peek test: {}".format(q.peek()))
    print("***Insert '21' to the back of the queue: ")
    q.insert(21)
    for v in q:
        print(v)
    # print the results of the method calls and verify by hand
    return

def array_to_pq(pq,a):
    for _ in range(len(a)):
        value = a.pop()
        pq.insert(value)
    return

def pq_to_array(pq, a):
    while pq.is_empty() != True:
        a.insert(pq.remove())
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of PriorityQueue are tested for both empty and 
        non-empty priority queues using the data in a:
        empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = PriorityQueue()

    # tests for the priority queue methods go here
    print("***Is_empty test 1: {}".format(pq.is_empty()))
    print("***Array_to_queue ->")
    array_to_pq(pq, a)
    print("***Is_empty test 2: {}".format(pq.is_empty()))

    print("***Tests remove(): {}".format(pq.remove()))
    print("***Peek test: {}".format(pq.peek()))
    # print the results of the method calls and verify by hand
    print('***Alphabetical test:')
    while not pq.is_empty():
        item = pq.remove()
        print(item)

    return

def array_to_list(l, a):
    for i in a:
        l.insert(999,i)
    return
    
def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    Use: list_test(a)
    -------------------------------------------------------
    Preconditions:
        a - list of data (list of ?)
    Postconditions:
        the methods of List are tested for both empty and 
        non-empty lists using the data in a:
        empty, insert, remove, append, index, __contains__,
        find, max, min, __getitem__, __setitem__
    -------------------------------------------------------
    """
    l = List()
    
    # tests for the List methods go here
    print("************Is_empty test: {}".format(l.is_empty()))
    print("************Insert test: ")
    array_to_list(l, a)

    l.insert(0, a[0])
    for v in l:
        
        print(v)
    print("************Is_empty test 2: {}".format(l.is_empty()))
    print("************Remove test: ")
    chicken_wings = Food("Chicken Wings", 8, None, None)
    l.remove(chicken_wings)
    for v in l:
        print(v)
    print("************Append test (Banana food object): ")
    banana = Food('Bananas', 0, None, None)
    l.append(banana)
    print("************Index test: {}".format(l.index(banana)))
    print("************Contains test: {}".format(banana in l))
    print("************Find test: {}".format(l.find(banana)))
    print("************Max test: {}".format(l.max()))
    print("************Min test: {}".format(l.min()))
    print("************Get_item test: {}".format(l[len(l)-1]))
    print("************Set_item test: ")
    cookie = Food('Cookies', 1, None, None)
    l[len(l)-1] = cookie
    for v in l:
        print(v)
    
    # print the results of the method calls and verify by hand

    return

def array_to_cq(cq, a):
    for _ in range(len(a)):
        value = a.pop(0)
        cq.insert(value)
    return
    
def cq_to_array(cq, a):
    while cq.is_empty() != True:
        a.append(cq.remove())
    return

def queue_circular_test(a):
    cq = CircularQueue(6)
    
    print("Is_empty test: {}".format(cq.is_empty()))
    print("Is_full test: {}".format(cq.is_full()))
    print("Insert test: ")
    array_to_cq(cq, a)
    for i in cq:
        print(i)
    print("Remove test: {}".format(cq.remove()))
    print("Peek test: {}".format(cq.peek()))
    for i in cq:
        print(i)