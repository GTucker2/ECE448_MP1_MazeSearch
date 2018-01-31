import createmaze
import MazeTree

# Get the maze to traverse
filename = input("Please enter the name of the mazefile (.txt): ")              

# Declare an array for the maze ascii data and then load significant info into an obj
ascii_maze = []                                                                      
mazeinfo = createmaze.loadMaze(filename, ascii_maze)      

# Create a graph based on the maze data
maze_tree = MazeTree.MazeTree()                                                
maze_tree = maze_tree.create_tree(ascii_maze, mazeinfo.startpx, mazeinfo.startpy )