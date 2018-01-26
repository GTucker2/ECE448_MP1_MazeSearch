#Kaleb Henderson
#Code for reading in the maze files and parsing them into a useful 2d array (really a list of lists)


#To Do Still: Figure out how to get the starting and ending points into my class
#             Possibly figure out a more efficient way of doing this


#class that holds all the relevant matrix info (height, width, starting and ending points
class mInfo:
    def __init__(self, height, width, spx, spy, epx, epy):
        self.h = height
        self.w = width
        self.startpx = spx
        self.startpy = spy
        self.endpx = epx
        self.endpy = epy

#function that takes given filename and parses the maze from that textfile while
# initializing the "2d array"
def loadMaze(filename, maze):               
    with open(filename) as inmaze:
        mazefile = inmaze.readlines()

    height = len(mazefile)
    chars = 0

    for line in mazefile:                   #gets the number of characters in the maze to calculate width (Possibly a more efficient way of doing this)
        #print(line),                       #prints maze to console without having to save it anywhere
        chars = chars + len(line)
 
    #print(height)                                  #checking if I got the height right
    width = int(chars/height)                       #calculating the width
    print(width)
    mazeinfo = mInfo(height, width, 0, 0, 0, 0)     #initializing the mInfo class with it's relevant info
    
    for column in mazefile:                     #sets up 2d matrix
        column = column.strip()                 #NOTE!!: these 4 lines may need to be rewritten/removed because I found in on stackoverflow and I am not 
        row = [i for i in column]               # sure what the rules are if you cite your code but if we can't do that then I'll have to figure out a 
        maze.append(row)                        # different way    
                                                #Link: https://stackoverflow.com/questions/40943108/reading-a-maze-file-in-python-and-printing-out-the-maze-line-by-line
    
    return mazeinfo                         #returns the class so that it is useful outside of this function
        



filename = input("Please enter the name of the mazefile (.txt): ")              #gets the file name from the user
maze = []                                                                       #creates the 1d matrix   
mazeinfo = loadMaze(filename, maze)                                             #first function loads the maze and finds the height and width

for i in range(0, mazeinfo.h):                                  #prints out the read in textfile
    for j in range(0, mazeinfo.w):                              #basically proves that I read in the file correctly
        print(maze[i][j], end="")                               # and made 2d accesible S
    print()                                                     #prints a newline at the end of the row

#print("Testing...")  #following code tests class object is working
#print(mazeinfo.h)
#print(mazeinfo.w)
#print(mazeinfo.endpx)

 

