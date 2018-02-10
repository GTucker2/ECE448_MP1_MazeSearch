## author : Michael Racine 
## date: 1/28/18

## Class that represents a tree filled with nodes created from a maze
class MazeTree:

    # initilize the nodes
    # param: self
    # return: initialized "MazeTree" hence refered to as a node
    def __init__(self):
        self.data = 'empty'
        self.x = -1
        self.y = -1
        self.f = -1
        self.g = -1
        self.h = -1
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited_from = "not"
        self.traversed = False 

    # create a node given data and coordinates
    # param: data - the string the node should store
    #        x    - the x coordinate of the node
    #        y    - the y coordinate of the node
    # return: the created node
    def create_node(data, x, y):
       node = MazeTree()
       node.data = data
       node.x = x
       node.y = y
       return node

    # create the tree based on data
    # param: maze      - 2d array of strings
    #        start_x   - the x position of the starting point
    #        start_y   - the y postiion of the starting point
    # return: the root of the tree/graph
    def create_tree(self, maze, mazeInfo, start_x, start_y):
        # initilize 2d array and fill with tree nodes; the data doesn't matter so just do the index 0,0 for all
        node_array = [[MazeTree.create_node(maze[0][0], 0, 0) for y in range(mazeInfo.w)] for x in range(mazeInfo.h)] 
 
        # put the correct node in the corresponding index
        for x in range(0, mazeInfo.h):
            for y in range(0, mazeInfo.w):
                node_array[x][y] = MazeTree.create_node(maze[x][y], x, y)

        # create the full tree/graph from the array
        for x in range(1, mazeInfo.h-1):
            for y in range(1, mazeInfo.w-1):
                # nodes should point to the walls but the walls shouldn't point to anything
                #if node_array[x][y].data != '%': #this makes the % nodes have no children. If we want to change it back just remove the comment
                node_array[x][y].up = node_array[x-1][y]
                node_array[x][y].down = node_array[x+1][y]
                node_array[x][y].left = node_array[x][y-1]
                node_array[x][y].right = node_array[x][y+1]

        # return the node array
        return node_array