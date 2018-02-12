import createmaze
import search
import consts
import MazeTree

class sd_dict:
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
                # every time, get a new maze 
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
                val = search.a_star(maze_copy, mazeinfo, maze_tree_copy, root, goal)
                if (end, start) not in self.dict and end != start: 
                    self.dict[(start, end)] = val[consts.STEPS_TAKEN_IDX()]
                    #print(str(start_point) + ":" + str(end_point) + ":" + str(val[consts.STEPS_TAKEN_IDX()]))

    def get_min_sd(self, curx, cury):
        start_pt = (curx, cury)
        relavent_weights = []
        for key in self.dict.keys():
            if key[0] == start_pt:
                relavent_weights.append(self.dict[key])
        return min(relavent_weights)

class dict_mst:
    def __init__(self):
        self.data = 'empty'
        self.x = -1
        self.y = -1
        self.neighbors = {}
        self.traversed = False

    def create_node(data, x, y):
        node = dict_mst()
        node.data = data
        node.x = x
        node.y = y
        return node

    def create_mst(self, sd_dict):
        edges = list(sd_dict.keys())
        nodes = {}
        while len(edges) > 0:
            min_edge = min(edges)
            if min_edge[0] not in nodes and min_edge[1] not in nodes:
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
                    node_unrep = min_edge[0]
                elif min_edge[1] not in nodes and min_edge[0] in nodes:
                    node_unrep = min_edge[1]
                x = node_unrep[0]                                              # Get the x value of the unrepresented node
                y = node_unrep[1]                                              # Get the y value of the unrepresented node
                nodes[node_unrep] = dict_mst.create_node('.', x, y)            # Create the unrepresented node
                nodes[min_edge[0]].neighbors[min_edge[1]] = nodes[min_edge[1]] # Create the edge representation 
                nodes[min_edge[1]].neighbors[min_edge[0]] = nodes[min_edge[0]] # Create the reverse edge representation
            edges.remove(min_edge)
        return nodes

    def sum_weights(self, mst_dict, sd_dict):
        seen_edges = []
        total_weight = 0
        for key in mst_dict.keys():
            start = (key[0],key[1]) 
            for neighbor in mst_dict[key].neighbors.values():
                end = (neighbor.x, neighbor.y)
                if ((start, end)) not in seen_edges and ((end, start)) not in seen_edges:
                    if neighbor.traversed is False:
                        total_weight += sd_dict.dict[(start, end)]
                    seen_edges.append((start,end))
                    seen_edges.append((end,start))
        return total_weight
                

