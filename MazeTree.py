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
        if start_x < 0:
            return None
        if start_x > len(maze):
            return None
        if start_y < 0:
            return None
        if start_y > len(maze[0]):
            return None

        ret_tree = create_node(maze[start_x][start_y], start_x, start_y)
        #recurse to create the children
        ret_tree.up = create_tree(maze, start_x, start_y+1)
        ret_tree.down = create_tree(maze, start_x, start_y-1)
        ret_tree.left = create_tree(maze, start_x-1, start_y)
        ret_tree.right = create_tree(maze, start_x+1, start_y)
        #return the root of the tree
        return ret_tree