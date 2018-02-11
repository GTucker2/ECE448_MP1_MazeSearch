# Kaleb Henderson
# Code for reading in the maze files and parsing them into a useful 2d array (really a list of lists)


# class that holds all the relevant matrix info (height, width, starting and ending points)
class mInfo:
    def __init__(self, height, width, spx, spy, epx, epy):
        self.h = height
        self.w = width
        self.startpx = spx
        self.startpy = spy
        self.endpx = epx
        self.endpy = epy

# function that takes given filename and parses the maze from that textfile while
# initializing the "2d array"
def loadMaze(filename, maze):               
    with open(filename) as inmaze:
        mazefile = inmaze.readlines()

    height = len(mazefile)
    chars = 0

    for line in mazefile:                           #gets the number of characters in the maze to calculate width
        chars = chars + len(line)
 
    width = int(chars/height)                       #calculating the width
    endpx = []
    endpy = []
    mazeinfo = mInfo(height, width, 0, 0, endpx, endpy)     #initializing the mInfo class with it's relevant info
    
    for column in mazefile:                         #sets up 2d matrix
        column = column.strip()                     #These 4 lines of code are from the following link
        row = [i for i in column]                   #Link: https://stackoverflow.com/questions/40943108/reading-a-maze-file-in-python-and-printing-out-the-maze-line-by-line
        maze.append(row)                            #
    
    
    for i in range(0, mazeinfo.h):
        for j in range(0, mazeinfo.w):                              
            if maze[i][j] == 'P':                                   #gets the x,y coordinates of the starting point
                mazeinfo.startpx = i
                mazeinfo.startpy = j
            elif maze[i][j] == '.':                                   #gets the x,y coordinates of all ending points and store them
                mazeinfo.endpx.append(i)                              #in separate x, y lists
                mazeinfo.endpy.append(j)
                
            
    
    return mazeinfo                                 #returns the class so that it is useful outside of this function

def print_maze(maze, NodesExp_StepsTaken, file_name):
    ''' print_maze
        Griffin A. Tucker
        Runs through a given array of mazedata and prints it to console
        Accepts: 
            maze : a 2D array of character maze data
            nodes_expanded : the number of nodes expanded in a
                performed search on the maze. 
            file_name : the name of the file to be exported
        Returns:
            1 : if no errors
            0 : if errors, i.e. the maze array is not valid
    '''
    # If the given array is null, return 0; otherwise traverse
    # and print the characters in the array.
    if maze is None:
        return 0
    else:
        # Declare a file to write to 
        fo = open(file_name, "w")
        # Write line by line 
        for i in range(0, len(maze)):
            if maze[0] is None:
                return 0
            else:
                for j in range(0, len(maze[0])):
                    if maze[i][j] is None:
                        return 0
                    else:
                        fo.write(maze[i][j])
            fo.write('\n')
        # Write the # nodes visited to the output solution
        fo.write("Nodes expanded: " + str(NodesExp_StepsTaken[0]) + ' \n')
        fo.write("Steps taken: " + str(NodesExp_StepsTaken[1]) + ' \n') 
        fo.write('\n')
    # Return successful 
    fo.close()
    return 1

def copy_maze(maze):
    '''
        Kaleb Henderson
        Function takes in a 2d ascii maze and makes another
        2d ascii copy
        Input:  maze - 2d array of maze characters
        Output: a 2d array that is a copy of the input maze array
    '''
    mazecopy = list.copy(maze)
    return mazecopy
    




 

