# ECE448_MP1_MazeSearch
ECE448 MP1; search algorithms on trees. 

## Authors
* **Griffin A. Tucker**  - [GTucker2](https://github.com/GTucker2)
* **Michael Racine** - [JotaroCooljo](https://github.com/JotaroCooljo)
* **Kaleb Henderson** - [kalebh9614](https://github.com/kalebh9614)

## Files

Note: The files cataloged here are only those which have been written by the developers and external parties. System-generated files will not be listed.

### Primary
The top level of the project directory. All main project files may be found here as well as the project documentation.
#### Documentation
* [README.md](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/README.md) - Summary of project and project contents
#### Project
* [main.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/main.py) - Main function; handles most if not all user interaction 
* [search.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/search.py) - Functions to perform BFS, DFS, greedy-first search, and A* search on mazes, and their helper functions 
* [createmaze.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/createmaze.py) - Functions to read-in and print-out text-maze files
* [MazeTree.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/MazeTree.py) - Class that represents a tree filled with nodes created from a maze
* [queue.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/queue.py) - Python queue implementation; see acknowledgements
* [stack.py](https://github.com/GTucker2/ECE448_MP1_MazeSearch/blob/master/stack.py) - Python stack implementation; see acknowledgements

### Tests 
This subdirectory holds a series of text maze files to run tests on.

### Solutions 
This subdirectory holds the produced solutions to the text maze files located in the Tests directory.

## Acknowledgements
* **Brad Miller, David Ranum** - [Python Queue Implementation](http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaQueueinPython.html)
* **Brad Miller, David Ranum** - [Python Stack Implementation](http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html)
