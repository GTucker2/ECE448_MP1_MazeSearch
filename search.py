import stack
import queue
import heapq
import math
import sd_dict
import MazeTree
import createmaze

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
                return (nodes_expanded, retrace(cur, maze_data, True))
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
    return (nodes_expanded, 0) 

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
                return (nodes_expanded, retrace(cur, maze_data, True))
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
    return (nodes_expanded, 0) 

def greedy_first(maze_data, root, goals):
    ''' greedy_first
        Griffin A. Tucker
        February 6 2018
        This function performs a greedy-first search on
            a given graph.
        Accepts:
            maze_data : a 2d array of characters 
            root  : a tree to perform the search on
            goals  :
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
            if cur.data is '.': return (nodes_expanded, retrace(cur, maze_data, True))
            else:
                nodes_expanded += 1
                if cur.up is not None and cur.up.data is not '%':
                    greedy_paths.append(cur.up)
                    if cur.up.visited_from == "not":
                        cur.up.visited_from = "down"
                if cur.down is not None and cur.down.data is not '%':
                    greedy_paths.append(cur.down)
                    if cur.down.visited_from == "not":
                        cur.down.visited_from = "up"
                if cur.left is not None and cur.left.data is not '%':
                    greedy_paths.append(cur.left)
                    if cur.left.visited_from == "not":
                        cur.left.visited_from = "right"
                if cur.right is not None and cur.right.data is not '%':
                    greedy_paths.append(cur.right)
                    if cur.right.visited_from == "not":
                        cur.right.visited_from = "left"
                q = h_enqueue(q, greedy_paths, goals, manhattan_distance)
                cur.traversed = True 
                greedy_paths = [] 

    # Return the negative number of nodes expanded since goal not found
    nodes_expanded *= -1
    return (nodes_expanded, 0)

def a_star(maze_data, mazeinfo, maze_tree, root, goals, do_print):
    ''' a_star
        Griffin A. Tucker
        FINAL DATE
        This function performs an A* search on a given
             graph.
        Accepts:
            maze_data : a 2d array of characters 
            root  : a tree to perform the search on
            goal  : a goal character value to search for
        Returns:
            1 : if the goal is found
            0 : if the goal is not found
        This function returns 0 for now.
    '''
    # Check if the tree is valid. If it is not, return 0.
    if root is None: return 0
    else: root.visited_from = "root"

    # If we have more than one goal, generate actual distances
    # between points as the heuristic model. Otherwise, use
    # the manhattan distance
    if len(goals[0]) > 1: 
        sd_values = sd_dict.sd_dict(maze_data, maze_tree, mazeinfo) 
        mst_obj = sd_dict.dict_mst()
        mst_dict = mst_obj.create_mst(sd_values.dict)
        return a_star_mult(maze_data, mazeinfo, maze_tree, sd_values, mst_dict, (root.x, root.y))

    # Declare a list and append the starting node.
    q = []     
    q.append(root)    

    # Save the root as the current location of the traversal
    cur = root

    # Create a list to store neighbors of the current node
    neighbors = []

    # Declare a counter for the number of nodes expanded. 
    # Set it to zero.
    nodes_expanded = 0

    # g is the cost of going from one node to the next
    # f is the total cost of getting from the start to the goal
    # by passing a node CHANGE FOR MULTIPLE NODES
    g = {}
    f = {}
    g[(root.x, root.y)] = 0
    f[(root.x, root.y)] = manhattan_distance(root.x, goals[0][0], root.y, goals[1][0])

    # While the q is not empty, get the next node on the queue
    # and check for the goal. If at the goal, copy the successful
    # path to the array of mazedata and then return 1. Else,
    # expand the node to the queue. 
    while len(q) > 0:
        min_val = None
        neighbors = []
        for node in q:
            if min_val is None or f[(node.x, node.y)] <= f[(cur.x, cur.y)]:
                min_val = f[(node.x, node.y)]
                cur = node
        q.remove(cur) 
        if (cur.x, cur.y) == (goals[0][0],goals[1][0]): 
            return (nodes_expanded, retrace(cur, maze_data, do_print))
        nodes_expanded += 1
        neighbors.append(cur.up)
        neighbors.append(cur.down)
        neighbors.append(cur.right)
        neighbors.append(cur.left)
        for neighbor in neighbors:
            if neighbor is not None and neighbor.data is not '%':
                if neighbor.traversed is False:
                    q.append(neighbor)
                    if neighbor.visited_from == "not":
                        if neighbor.up == cur: neighbor.visited_from = "up"
                        elif neighbor.down == cur: neighbor.visited_from = "down"
                        elif neighbor.left == cur: neighbor.visited_from = "left"
                        elif neighbor.right == cur: neighbor.visited_from = "right"
                g_tentative = g[(cur.x, cur.y)] + 1
                if(neighbor.x, neighbor.y) not in g or g_tentative < g[(neighbor.x, neighbor.y)]:
                    g[(neighbor.x, neighbor.y)] = g_tentative
                    f[(neighbor.x, neighbor.y)] = g_tentative + manhattan_distance(neighbor.x, goals[0][0], neighbor.y, goals[1][0])
        cur.traversed = True
        
    print("here")

    # Return the negative number of expanded nodes since no goal found
    nodes_expanded *= -1
    return (nodes_expanded, 0)

def a_star_mult(maze_data, mazeinfo, maze_tree, sd_data, mst_data, start_xy):

    # Create a q to search over
    q = []
    q.append(start_xy)

    # set the current traversed nodes xy and set it as traversed
    cur_xy = start_xy
    mst_data[start_xy].traversed = True 
    mst_obj = sd_dict.dict_mst()

    # g is the cost of going from one node to the next
    # f is the total cost of getting from the start to the goal
    # by passing a node CHANGE FOR MULTIPLE NODES
    g = {}
    f = {}
    g[start_xy] = 0
    f[start_xy] = sd_data.get_min_sd(start_xy[0], start_xy[1]) + mst_obj.sum_weights(mst_data, sd_data)

    # Search for the optimal retrace_path
    unvisited = list(mst_data.keys())
    
    # Keep track of steps taken
    last_node = start_xy
    callback_list = []
    
    min_val = None
    while len(q) > 0:
        if len(q) == 1: 
            cur_xy = q[0]
        else:
            cur_xy = q[0]
            for node_xy in q:
                if min_val is None or f[node_xy] <= f[cur_xy]:
                    min_val = f[node_xy]
                    cur_xy = node_xy
        callback_list.append((last_node, cur_xy))
        last_node = cur_xy
        if cur_xy in unvisited: unvisited.remove(cur_xy)
        q.remove(cur_xy) 
        if len(unvisited) == 0: 
            return a_star_mult_retrace(maze_data, mazeinfo, maze_tree, mst_data, cur_xy, callback_list)
        for neighbor_xy in mst_data[cur_xy].neighbors.keys():
            if neighbor_xy is not None:
                if mst_data[cur_xy].neighbors[neighbor_xy].traversed is False:
                    q.append(neighbor_xy)
                    if mst_data[cur_xy].neighbors[neighbor_xy].visited_from == (-1,-1):
                        mst_data[cur_xy].neighbors[neighbor_xy].visited_from = cur_xy
                if (cur_xy, neighbor_xy) in sd_data.dict:
                    g_tentative = g[cur_xy] + sd_data.dict[cur_xy, neighbor_xy]
                else:
                    g_tentative = g[cur_xy] + sd_data.dict[neighbor_xy, cur_xy]
                if neighbor_xy not in g or g_tentative < g[neighbor_xy]:
                    g[neighbor_xy] = g_tentative
                    f[neighbor_xy] = g_tentative + sd_data.get_min_sd(neighbor_xy[0], neighbor_xy[1]) + mst_obj.sum_weights(mst_data, sd_data)
        mst_data[cur_xy].traversed = True 

    return a_star_mult_retrace(maze_data, mazeinfo, maze_tree, mst_data, cur_xy)

def retrace(goal, maze_data, do_print):
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

    # Instantiate a step counter 
    steps_taken = 0 

    # Set the current node being visited as the provided
    # goal node.
    cur = goal

    # Traverse a back path from the goal node to the start
    # node. 
    while cur.visited_from is not 'root':
        steps_taken += 1
        if cur.visited_from == "down":
            cur = cur.down
        elif cur.visited_from == "up":
            cur = cur.up
        elif cur.visited_from == "right":
            cur = cur.right
        elif cur.visited_from == "left":
            cur = cur.left 
        elif cur.visited_from == "not":
            return 0
        if cur.data is not '.' and cur.data is not 'P' and do_print is True:
            maze_data[cur.x][cur.y] = '.'
    # Return successful
    return steps_taken

def a_star_mult_retrace(maze_data, mazeinfo, maze_tree, mst_data, start_xy, callback_list):
    
    # declare useful constants
    root_xy = (-1, -1)
    markers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    marker_i = len(mazeinfo.endpx) - 1
    callback_i = len(callback_list) - 1
    steps_taken = 0
    cur_xy = callback_list[callback_i][1]
    unvisited = list(mst_data.keys())
    
    while callback_i >= 0:
        if callback_list[callback_i][0] != callback_list[callback_i][1]:
            #print(str(callback_list[callback_i][0]) + " : " + str(callback_list[callback_i][1]))
            root = maze_tree[cur_xy[0]][cur_xy[1]]
            goal_x = []
            goal_y = []
            goal_x.append(callback_list[callback_i][0][0])
            goal_y.append(callback_list[callback_i][0][1])
            goal_xy = (goal_x, goal_y)
            createmaze.reset_vals(maze_tree)
            ret = a_star(maze_data, mazeinfo, maze_tree, root, goal_xy, True)
            steps_taken += ret[1]
            #print(steps_taken)
            if cur_xy in unvisited:
                maze_data[cur_xy[0]][cur_xy[1]] = markers[marker_i] 
                marker_i -= 1
                unvisited.remove(cur_xy)
        callback_i -= 1
        cur_xy = callback_list[callback_i][1]

    return (0, steps_taken)

def manhattan_distance(curx, goalx, cury, goaly):
    '''
       Function finds the manhattan distance between the point passed and the 
       end point of the maze.
       Returns that value
    '''
    return abs(goalx - curx) + abs(goaly - cury)

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

    # for i in range(0, len(Q)):
    #    print(str(Q[i].x))

    # Create and fill a list of heuristic values 
    # Copy the states (we do not want to modify the original set)
    h_vals = []
    Q_copy = []
    for state_idx in range(0, len(Q)):
        new_q = Q[state_idx]
        Q_copy.append(new_q)
        h_vals.append(h(new_q.x, A[0][0], new_q.y, A[1][0]))

    # Enqueue onto the queue each state q in Q (sorry) based on sorted
    # h values of the states.
    while len(Q_copy) > 0:
        best_h = min(h_vals) 
        best_q = Q_copy[h_vals.index(best_h)]
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
