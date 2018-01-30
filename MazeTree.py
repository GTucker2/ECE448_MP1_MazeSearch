## author : Michael Racine 
## date: 1/28/18


class MazeTree:

    #initilize the nodes
    def __init__(self):
        self.data = None
        self.x = None
        self.y = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.visited = False

    #create a node given data and coordinates
    def create_node(data, x, y):
       node = MazeTree()
       node.data = data
       node.x = x
       node.y = y
       return node

    #create the tree based on data
    def create_tree(self, maze, start_x, start_y):
        #base cases. check if x,y are in the bounds of the maze and if the maze exists
        if maze is None:
            return None
        x_max = len(maze)
        y_max = len(maze[0])
        if start_x < 0:
            return None
        elif start_x >= x_max:
            return None
        if start_y < 0:
            return None
        elif start_y >= y_max:
            return None

        print(start_x)
        print(start_y)
        
        ret_tree = MazeTree.create_node(maze[start_x][start_y], start_x, start_y)
        #recurse to create the children
        up = start_y + 1
        down = start_y - 1
        left = start_x - 1
        right = start_x + 1
        ret_tree.up = MazeTree.create_tree(self, maze, start_x, up)
        ret_tree.down = MazeTree.create_tree(self, maze, start_x, down)
        ret_tree.left = MazeTree.create_tree(self, maze, left, start_y)
        ret_tree.right = MazeTree.create_tree(self, maze, right, start_y)
        #return the root of the tree
        return ret_tree