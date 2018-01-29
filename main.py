import createmaze
import MazeTree

# Get the maze to traverse
filename = input("Please enter the name of the mazefile (.txt): ")              

# Declare an array for the maze ascii data and then load significant info into an obj
ascii_maze = []                                                                      
mazeinfo = createmaze.loadMaze(filename, ascii_maze)                    
for i in range(0, mazeinfo.h):                                  #prints out the read in textfile
    for j in range(0, mazeinfo.w):                              #basically proves that I read in the file correctly
        if ascii_maze[i][j] == 'P':                                   #gets the x,y coordinates of the starting point
            mazeinfo.startpx = i
            mazeinfo.startpy = j
        if ascii_maze[i][j] == '.':                                   #gets the x,y coordinates of the ending point
            mazeinfo.endpx = i                                  #NOTE: Does not work with the multiple endpoint mazes, still need to work on that.
            mazeinfo.endpy = j
        #print(ascii_maze[i][j], end="")                               # and made a 2d accesible maze
    #print() 

print(mazeinfo.h)
print(mazeinfo.w)
print()

# Create a graph based on the maze data
maze_tree = MazeTree.MazeTree()
maze_tree = maze_tree.create_tree(ascii_maze, mazeinfo.startpx, mazeinfo.startpy)                                                    #prints a newline at the end of the row

#print(tree_root.data)