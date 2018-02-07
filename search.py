import stack
import queue
import heapq
import math

''' search.py
    Griffin A. Tucker
    FINAL DATE
    This module allows the user to perform a set 
        of searches on a given graph. The
        implemented searches include the following:
        bredth-first search, depth-first search,
        greedy-first search, and A* search. 
'''
#YOU SPELLED IT WRONG BOI
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
            The total number of expanded nodes. 
                If > 0: the goal was found
                If <= 0: the goal was not found
    '''
    # Check if the tree is valid. If it is not, return 0.
    if root is None: return 0
    else: root.visited_from = "root"

    # Declare a queue and enqueue the starting node.
    q = queue.Queue()         
    q.enqueue(root)    

    # Declare a counter for the number of nodes expanded. 
    # Set it to zero.
    nodes_expanded = 0

    # While the q is not empty, get the next node on the queue
    # and check for the goal. If at the goal, copy the successful
    # path to the array of mazedata and then return 1. Else,
    # expand the node to the queue. 
    while q.size() > 0:       
        cur = q.dequeue() 
        if cur.traversed is False:
            if cur.data is 'P': cur.traversed = True
            if cur.data is goal: 
                retrace(cur, maze_data)
                return nodes_expanded 
            else:    
                nodes_expanded += 1       
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

    # Return the negative number of expanded nodes since no goal found
    nodes_expanded *= -1
    return nodes_expanded 

def depth_first(maze_data, root, goal):
    ''' depth_first
        Griffin A. Tucker
        February 3 2018
        This function performs a depth-first search on
            a given graph.
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
    else: root.visited_from = "root"

    # Declare a stack and push the root node
    s = stack.Stack()
    s.push(root)

    # Declare a counter for the number of nodes expanded. 
    # Set it to zero.
    nodes_expanded = 0

    # While the stack is not empty, get the next node on the stack
    # and check for the goal. If at the goal, copy the successful
    # path to the array of mazedata and then return 1. Else,
    # expand the node to the stack. 
    while s.size() > 0:  
        cur = s.pop()
        if cur.traversed is False:
            if cur.data is 'P': cur.traversed = True
            if cur.data is goal: 
                retrace(cur, maze_data)
                return nodes_expanded
            else:       
                nodes_expanded += 1          
                if cur.up is not None and cur.up.data is not '%': 
                    s.push(cur.up)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "down"
                if cur.down is not None and cur.down.data is not '%': 
                    s.push(cur.down)
                    if cur.down.visited_from == "not":
                        cur.down.visited_from = "up"
                if cur.left is not None and cur.left.data is not '%': 
                    s.push(cur.left)
                    if cur.left.visited_from == "not":
                        cur.left.visited_from = "right"
                if cur.right is not None and cur.right.data is not '%': 
                    s.push(cur.right)
                    if cur.right.visited_from == "not":
                        cur.right.visited_from = "left"
            cur.traversed = True

    # Return the number of nodes expanded; negative since no goal found
    nodes_expanded *= -1
    return nodes_expanded 

def greedy_first(maze_data, root, goal):
    ''' greedy_first
        Griffin A. Tucker
        February 6 2018
        This function performs a greedy-first search on
            a given graph.
        Accepts:
            maze_data : a 2d array of characters 
            root  : a tree to perform the search on
            goal  : a goal character value to search for
        Returns:
            The total number of nodes expanded during the seach.
            This value is negative or 0 if the goal was not found.
    '''
    # Check if the tree is valid. If it is not, return 0
    if root is None: return 0
    else: root.visited_from = "root"
    
    # Declare a queue and enqueue the starting node
    q = queue.Queue()
    q.enqueue(root)

    # Declare a list for sorting node paths based on heuristic
    greedy_paths = []

    # Declare a counter for the number of nodes expanded. 
    # Set it to zero.
    nodes_expanded = 0  

    # While the q is not empty, get the next node on the queue
    # and check for the goal. If at the goal, copy the successful
    # path to the array of mazedata and then return 1. Else, expand
    # the node based on the manhattan distance heuristic.a_star
    while q.size() > 0:
        cur = q.dequeue()
        if cur.traversed is False:
            if cur.data is 'P': cur.traversed = True
            if cur.data is goal:
                retrace(cur, maze_data)
                return nodes_expanded
            else:
                nodes_expanded += 1
                if cur.up is not None and cur.up.data is not '%':
                    greedy_paths.append(cur.up)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "down"
                if cur.down is not None and cur.up.data is not '%':
                    greedy_paths.append(cur.down)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "up"
                if cur.left is not None and cur.up.data is not '%':
                    greedy_paths.append(cur.left)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "right"
                if cur.right is not None and cur.up.data is not '%':
                    greedy_paths.append(cur.right)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "left"
                q = h_enqueue(q, greedy_paths, goal, manhattan_distance)
                cur.traversed = True 
                greedy_paths = [] 

    # Return the negative number of nodes expanded since goal not found
    nodes_expanded *= -1
    return nodes_expanded

def a_star(mazeinfo):
    ''' a_star
        Michael Racine
        FINAL DATE
        This function performs an A* search on a given
             graph.
        This function returns 0 for now.
    '''

    mhd = astar_heuristic(
    print(mhd)
    return 0

def retrace(goal, maze_data):
    ''' retrace
        Griffin A. Tucker
        February 3 2018
        This function alters an array of given mazedata
            so that it holds a return path from a goal
            to a start
        Accepts:
            maze_data : a 2d array of characters 
            goal  : a goal node to begin the retrace on
        Returns:
            1 : if we reach the start 
            0 : if data is invalid
    '''
    # Check that the supplied data is valid
    if goal is None or maze_data is None:
        return 0

    # Set the current node being visited as the provided
    # goal node.
    cur = goal

    # Traverse a back path from the goal node to the start
    # node. 
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

    # Return successful
    return 1

def manhattan_distance(cur, goal):
    '''
       Function finds the manhattan distance between the point passed and the 
       end point of the maze.
       Returns that value
    '''
    return abs(goal.x - cur.x) + abs(goal.y - cur.y)

def h_enqueue(queue, Q, A, h):
    ''' max_manhattan_remove
        Griffin A. Tucker
        Febraury 6 2018
        This function takes a set of states (Q) and enqueues them to
            a given queue based on a supploed heuristic (h) with respect
            to a given accept state (A)
        Accepts:
            queue : The queue to enqueue a set of states to
            Q : A set of states to be enqueued to the queue
            A : An accepting state with which to use the heuristic with
            h : A heuristic function to base the enqueue on 
        Returns:
            The queue with all states enqueued
    '''
    # Check for valid parameters. If we fail, return the unmodified queue
    if queue is None or Q is None or A is None or h is None:
        return queue

    # Create and fill a list of heuristic values 
    # Copy the states (we do not want to modify the original set)
    h_vals = []
    Q_copy = []
    for q in Q:
        Q_copy.append(q)
        h_vals.append(h(q,A))

    # Enqueue onto the queue each state q in Q (sorry) based on sorted
    # h values of the states.
    while len(Q_copy) > 0:
        best_h = min(h_vals) 
        best_q = Q_copy[Q_copy.index(best_h)]
        queue.enqueue(best_q)
        Q_copy.remove(best_q)
        h_vals.remove(best_h)

    # Return the final queue
    return queue

def astar_heuristic(cur, goal):
    '''
        Finds the Euclidian distance between two points
        Good heuristic for a single goal state
        but not sure how to translate to multiple
    '''
                          
    return math.sqrt((abs(goal.x - cur.x)**2) + (abs(goal.y - cur.y)**2))
