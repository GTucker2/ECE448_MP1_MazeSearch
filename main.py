import createmaze
import MazeTree
import search

# Get the maze to traverse
filename = input("Please enter the name of the mazefile (.txt): ")  

# Get the searchtype to perform on the maze
searchtype = "none"
searchtypes = ["BFS","DFS","GREEDY","ASTAR"]
while searchtype not in searchtypes:
    searchtype = input("Please enter the type of search you would like to perform: (BFS, DFS, GREEDY, ASTAR")  
    if searchtype not in searchtypes: print("Searchtype not found. Please enter BFS, DFS, GREEDY, or ASTAR: ")

# Declare an array for the maze ascii data and then load significant info into an obj
ascii_maze = []                                                                      
mazeinfo = createmaze.loadMaze(filename, ascii_maze)   

# Create a graph based on the maze data
maze_tree = MazeTree.MazeTree()                                                
maze_tree = maze_tree.create_tree(ascii_maze, mazeinfo, mazeinfo.startpx, mazeinfo.startpy)

# Perform a search on the maze and export solution
if searchtype is "BFS": search.bredth_first(ascii_maze, maze_tree, '.')
elif searchtype is "DFS": search.depth_first(ascii_maze, maze_tree, '.')
elif searchtype is "GREEDY": search.greedy_first()
elif searchtype is "ASTAR": search.a_star()
    a = 1
outputname = input(" Please enter the desired outputfile name (.txt) ")
createmaze.print_maze(ascii_maze, outputname)
