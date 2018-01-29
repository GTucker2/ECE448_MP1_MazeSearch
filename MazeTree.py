


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
            node = MazeTree.MazeNode()
            node.data = data
            node.x = x
            node.y = y
            return node

    #create default tree
    def __init__(self):
        self.root = MazeTree.MazeNode()

    #create the tree based on data
    def create_tree(self, maze, start_x, start_y):
        #base cases. check if x,y are in the bounds of the maze and if the maze exists
        if maze is None:
            return None
        if 0 > start_x:
            if start_x > len(maze):
                return None
        if 0 > start_y:
            if start_x > len(maze[0]):
                return None
        ret_tree = MazeTree()
        ret_tree.root = ret_tree.MazeNode.create_node(maze[start_x][start_y], start_x, start_y)
        #recurse to create the children
        up = start_y + 1
        down = start_y - 1
        left = start_x - 1
        right = start_x + 1
        ret_tree.root.up = ret_tree.create_tree(maze, start_x, up)
        ret_tree.root.down = ret_tree.create_tree(maze, start_x, down)
        ret_tree.root.left = ret_tree.create_tree(maze, left, start_y)
        ret_tree.root.right = ret_tree.create_tree(maze, right, start_y)
        return ret_tree.root