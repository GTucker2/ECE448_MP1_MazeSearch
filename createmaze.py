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
    mazeinfo = mInfo(height, width, 0, 0, 0, 0)     #initializing the mInfo class with it's relevant info
    
    for column in mazefile:                         #sets up 2d matrix
        column = column.strip()                     #These 4 lines of code are from the following link
        row = [i for i in column]                   #Link: https://stackoverflow.com/questions/40943108/reading-a-maze-file-in-python-and-printing-out-the-maze-line-by-line
        maze.append(row)                            #

    for i in range(0, mazeinfo.h):                                  #prints out the read in textfile
        for j in range(0, mazeinfo.w):                              #basically proves that I read in the file correctly
            if maze[i][j] == 'P':                                   #gets the x,y coordinates of the starting point
                mazeinfo.startpx = i
                mazeinfo.startpy = j
            if maze[i][j] == '.':                                   #gets the x,y coordinates of the ending point
                mazeinfo.endpx = i                                  #NOTE: Does not work with the multiple endpoint mazes, still need to work on that.
                mazeinfo.endpy = j
    
    return mazeinfo                                 #returns the class so that it is useful outside of this function

def print_maze(maze, file_name):
    ''' print_maze
        Griffin A. Tucker
        Runs through a given array of mazedata and prints it to console
        Accepts: 
            maze : a 2D array of character maze data
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

    # Return successful 
    fo.close()
    return 1
        




 

