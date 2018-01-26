


class MazeTree:

    #create node subclass
    class MazeNode:
        #initilize the nodes
        def __init__(self):
            self.data = None
            self.x = None
            self.y = None
            self.up = None
            self.down = None
            self.left = None
            self.right = None

        #create a node given data and coordinates
        def create_node(data, x, y):
            node = MazeNode()
            node.data = data
            node.x = x
            node.y = y
            return node

    #create default tree
    def __init__(self):
        self.root = MazeNode()

    #create the tree based on data
    def create_tree(maze, start_x, start_y):

        return