import stack
import queue

''' search.py
    Griffin A. Tucker
    FINAL DATE
    This module allows the user to perform a set 
        of searches on a given graph. The
        implemented searches include the following:
        bredth-first search, depth-first search,
        greedy-first search, and A* search. 
'''

def bredth_first(tree, start, goal):
    ''' bredth_first
        Griffin A. Tucker
        FINAL DATE
        This function performs a bredth-first search on
            a given graph.
        This function returns 0 for now.
    '''
    # Check if the tree is valid
    if tree is None: return 0

    # Declare a queue and enqueue the start tree 
    q = queue.Queue()
    q.enqueue(start) 

    # While the q is not empty 
    while q.size() > 0:
        # Get the current tree from the queue and check for success
        # If successful, return true. Otherwise, expand.
        cur = queue.dequeue()
        if cur is goal: 
            return 1
        else:
            if cur.up is not None: q.enqueue(cur.up)
            if cur.down is not None: q.enqueue(cur.down)
            if cur.left is not None: q.enqueue(cur.right)
            if cur.right is not None: q.enqueue(cur.left)
    
    # Return failure if goal was not found
    return 0

def depth_first():
    ''' depth_first
        Griffin A. Tucker
        FINAL DATE
        This function performs a depth-first search on
            a given graph.
        This function returns 0 for now.
    '''
    # Declare a stack
    s = stack.Stack()
    # Return result 
    return 0

def greedy_first():
    ''' greedy_first
        Griffin A. Tucker
        FINAL DATE
        This function performs a greedy-first search on
            a given graph.
        This function returns 0 for now.
    '''
    return 0

def a_star():
    ''' a_star
        Griffin A. Tucker
        FINAL DATE
        This function performs an A* search on a given
             graph.
        This function returns 0 for now.
    '''
    return 0