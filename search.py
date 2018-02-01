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

def bredth_first(maze_data, root, goal):
    ''' bredth_first
        Griffin A. Tucker
        January 25 2018
        Performs a bredth-first search on a given tree.
        Accepts:
            maze_data : a 2d array of characters 
            root  : a tree to perform the search on
            goal  : a goal character value to search for
        Returns:
            1 : if the goal is found
            0 : if the goal is not found
    '''
    # Check if the tree is valid. If it is not, return 0.
    if root is None: return 0
    else: 
        root.visited_from = "root"
        #root.traversed = True 

    # Declare a queue and enqueue the starting node.
    q = queue.Queue()         
    q.enqueue(root)    

    # While the q is not empty, get the next node on the queue
    # and check for the goal. If at the goal, copy the successful
    # path to the array of mazedata and then return 1. Else,
    # expand the node to the queue. 
    while q.size() > 0:       
        cur = q.dequeue() 
        if cur.traversed is False:
            if cur.data is 'P': cur.traversed = True
            if cur.data is goal: 
                while cur.data is not 'P':
                    if cur.visited_from == "down":
                        cur = cur.down
                    elif cur.visited_from == "up":
                        cur = cur.up
                    elif cur.visited_from == "right":
                        cur = cur.right
                    elif cur.visited_from == "left":
                        cur = cur.left 
                    if cur.data is not '.' and cur.data is not 'P':
                        maze_data[cur.x][cur.y] = '^'
                return 1
            else:                 
                if cur.up is not None and cur.up.data is not '%': 
                    q.enqueue(cur.up)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "down"
                if cur.down is not None and cur.down.data is not '%': 
                    q.enqueue(cur.down)
                    if cur.down.visited_from == "not":
                        cur.down.visited_from = "up"
                if cur.left is not None and cur.left.data is not '%': 
                    q.enqueue(cur.left)
                    if cur.left.visited_from == "not":
                        cur.left.visited_from = "right"
                if cur.right is not None and cur.right.data is not '%': 
                    q.enqueue(cur.right)
                    if cur.right.visited_from == "not":
                        cur.right.visited_from = "left"
            cur.traversed = True

    # Return 0 if goal was not found
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