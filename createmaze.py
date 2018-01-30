#Kaleb Henderson
#Code for reading in the maze files and parsing them into a useful 2d array (really a list of lists)


#class that holds all the relevant matrix info (height, width, starting and ending points)
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

    for line in mazefile:                   #gets the number of characters in the maze to calculate width
        #print(line),                       #prints maze to console without having to save it anywhere
        chars = chars + len(line
 
    #print(height)
    width = int(chars/height)                       #calculating the width
    #print(width)
    mazeinfo = mInfo(height, width, 0, 0, 0, 0)     #initializing the mInfo class with it's relevant info
    
    for column in mazefile:                     #sets up 2d matrix
        column = column.strip()                 #These 4 lines of code are from the following link
        row = [i for i in column]               #Link: https://stackoverflow.com/questions/40943108/reading-a-maze-file-in-python-and-printing-out-the-maze-line-by-line
        maze.append(row)                        #
    
    return mazeinfo                         #returns the class so that it is useful outside of this function
        




 

