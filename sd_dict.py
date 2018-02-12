import createmaze
import search
import consts
import MazeTree

''' sd_dict.py
    Griffin A. Tucker
    February 11 2018
    This module defines two structures: sd_dict and dict_mst.
'''
class sd_dict:
    ''' sd_dict  
        Griffin A. Tucker
        February 11 2018
        This class creates an object which holds a dictionary
        of path costs between start and end points in a graph. 
        This serves as a wrapper class for a typical 
        dictionary, filling the dict on instantiation.
    '''
    def __init__(self, maze_data, maze_tree, mazeinfo):
        # initialize a dictionary for storing all step distances between
        # significant points in the maze (all goals and the start)
        self.dict = {}

        # get all points to generate distances between
        points = []
        points.append((mazeinfo.startpx, mazeinfo.startpy))
        for cur_point in range(0, len(mazeinfo.endpx)):
            points.append((mazeinfo.endpx[cur_point], mazeinfo.endpy[cur_point]))

        # generate step distances between all points in the points array and store
        for start_point in range(0, len(points)):
            start = points[start_point]
            for end_point in range(0, len(points)):
                maze_copy = []
                maze_copy = createmaze.copy_maze(maze_data)
                root_r = MazeTree.MazeTree()
                maze_tree_copy = root_r.create_tree(maze_copy, mazeinfo, mazeinfo.startpx, mazeinfo.startpy)
                end = points[end_point]
                endx = []
                endy = []
                endx.append(end[0])
                endy.append(end[1])
                root = maze_tree_copy[start[0]][start[1]]
                goal = (endx, endy)
                val = search.a_star(maze_copy, mazeinfo, maze_tree_copy, root, goal, False)
                if (end, start) not in self.dict and end != start: 
                    self.dict[(start, end)] = val[consts.STEPS_TAKEN_IDX()]

    def get_min_sd(self, curx, cury):
        ''' get_min_sd   
            Griffin A. Tucker
            February 11 2018
            Return the minimum value for some start point 
                (curx, cury) in the dictionary
            Accepts:
                curx : the x coordinate of the start point
                cury : the y coordinate of the start point
            Returns:
                The minimum step cost with respect to 
                    (curx, cury) as a start point.
        '''
        start_pt = (curx, cury)
        relavent_weights = []
        for key in self.dict.keys():
            if key[0] == start_pt or key[1] == start_pt:
                relavent_weights.append(self.dict[key])
        return min(relavent_weights)

class dict_mst:
    ''' dict_mst
        Griffin A. Tucker
        February 11 2018
        This class creates an MST for some given dict
        of edge weight values (sd_dict)
    '''
    def __init__(self):
        self.data = 'empty'
        self.x = -1
        self.y = -1
        self.neighbors = {}
        self.traversed = False
        self.eaten = False
        self.visited_from = (-1,-1)

    def create_node(data, x, y):
        ''' create_node 
            Griffin A. Tucker
            February 11 2018
            Creates a node for the MST
            Accepts:
                x : the x position of the node in the maze
                y : the y position of the node in the maze
            Returns:
                The created node
        '''
        node = dict_mst()
        node.data = data
        node.x = x
        node.y = y
        return node

    def create_mst(self, sd_dict):
        ''' get_min_sd   
            Griffin A. Tucker
            February 11 2018
            Generates an MST for a given sd_dict
            Accepts:
                sd_dict : a dictionary of step cost
                    values for (x,y) keys
            Returns:
                The MST as a dict which allows 
                referencing of any node
        '''
        edges = list(sd_dict.keys())
        weights = list(sd_dict.values())
        node_sets = {}
        nodes = {}
        while len(edges) > 0:
            min_edge = edges[weights.index(min(weights))]
            if min_edge[0] not in nodes and min_edge[1] not in nodes:
                node_sets[min_edge[0]] = [min_edge[0], min_edge[1]]
                node_sets[min_edge[1]] = [min_edge[0], min_edge[1]]
                xA = min_edge[0][0]
                yA = min_edge[0][1]
                xB = min_edge[1][0]
                yB = min_edge[1][1]
                nodes[min_edge[0]] = dict_mst.create_node('.', xA, yA)
                nodes[min_edge[1]] = dict_mst.create_node('.', xB, yB)
                nodes[min_edge[0]].neighbors[min_edge[1]] = nodes[min_edge[1]] # Create the edge representation 
                nodes[min_edge[1]].neighbors[min_edge[0]] = nodes[min_edge[0]] # Create the reverse edge representation
            elif min_edge[0] not in nodes or min_edge[1] not in nodes:
                if min_edge[0] not in nodes and min_edge[1] in nodes: 
                    node_sets[min_edge[0]] = [min_edge[0], min_edge[1]]
                    node_sets[min_edge[1]].append(min_edge[0])
                    node_unrep = min_edge[0]
                elif min_edge[1] not in nodes and min_edge[0] in nodes:
                    node_sets[min_edge[0]].append(min_edge[1])
                    node_sets[min_edge[1]] = [min_edge[0], min_edge[1]]
                    node_unrep = min_edge[1]
                x = node_unrep[0]                                              # Get the x value of the unrepresented node
                y = node_unrep[1]                                              # Get the y value of the unrepresented node
                nodes[node_unrep] = dict_mst.create_node('.', x, y)            # Create the unrepresented node
                nodes[min_edge[0]].neighbors[min_edge[1]] = nodes[min_edge[1]] # Create the edge representation 
                nodes[min_edge[1]].neighbors[min_edge[0]] = nodes[min_edge[0]] # Create the reverse edge representation
            else:
                if min_edge[1] not in node_sets[min_edge[0]]:
                    for node in node_sets[min_edge[0]]:
                        node_sets[min_edge[1]].append(node)
                    for node in node_sets[min_edge[1]]:
                        node_sets[min_edge[0]].append(node)
                    nodes[min_edge[0]].neighbors[min_edge[1]] = nodes[min_edge[1]]
                    nodes[min_edge[1]].neighbors[min_edge[0]] = nodes[min_edge[0]]

            edges.remove(min_edge)
            weights.remove(min(weights))
        return nodes

    def sum_weights(self, mst_dict, sd_dict):
        ''' sum_weights
            Griffin A. Tucker
            February 11 2018
            Return the sum of all the untraversed edges in 
                the MST.
            Accepts:
                mst_dict : an MST as a dictionary
                sd_dict : a dictionary of step cost
                    values for (x,y) keys
            Returns:
                The sum of the untraversed edges in the MST
        '''
        seen_edges = []
        total_weight = 0
        for key in mst_dict.keys():
            start = (key[0],key[1]) 
            for neighbor in mst_dict[key].neighbors.values():
                end = (neighbor.x, neighbor.y)
                if ((start, end)) not in seen_edges and ((end, start)) not in seen_edges:
                    if neighbor.traversed is False:
                        if (start, end) in sd_dict.dict.keys(): 
                            total_weight += sd_dict.dict[(start, end)]
                        else:
                            total_weight += sd_dict.dict[(end, start)]
                    seen_edges.append((start,end))
                    seen_edges.append((end,start))
        return total_weight
                

