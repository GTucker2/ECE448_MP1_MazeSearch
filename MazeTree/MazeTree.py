


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
        #base cases. check if x,y are in the bounds of the maze and if the maze exists
        if maze == None:
            return None
        if 0 > start_x > len(maze):
            return None
        if 0 > start_y > len(maze[0]):
            return None
        ret_tree = MazeTree()
        ret_tree.root = MazeNode.create_node(maze[start_x][start_y], start_x, start_y)
        #recurse to create the children
        ret_tree.root.up = create_tree(maze, start_x, start_y+1)
        ret_tree.root.down = create_tree(maze, start_x, start_y-1)
        ret_tree.root.left = create_tree(maze, start_x-1, start_y)
        ret_tree.root.right = create_tree(maze, start_x+1, start_y)
        return ret_tree.root