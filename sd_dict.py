import createmaze
import search
import consts

class sd_dict:
    def __init__(self, maze_data, maze_tree, mazeinfo):
        # initialize a dictionary for storing all step distances between
        # significant points in the maze (all goals and the start)
        self.dict = {}

        # get all points to generate distances between
        points = []
        points.append((mazeinfo.startpx, mazeinfo.startpy))
        for cur_point in range(0, len(mazeinfo.endpx)):
            points.append((mazeinfo.endpx[cur_point], mazeinfo.endpy[cur_point]))

        # generate step distances between all points in the points array and store
        for start_point in range(0, len(points)):
            start = points[start_point]
            for end_point in range(0, len(points)):
                end = points[end_point]
                root = maze_tree[start[consts.X]][start[consts.Y]]
                goal = []
                goal.append(maze_tree[end[consts.X]][end[consts.Y]])
                val = a_star(maze_data, mazeinfo, maze_tree, root, goal)
                self.dict[(start, end)] = val[consts.STEPS_TAKEN_IDX]

    def get_sd(self, curx, goalx, cury, goaly):
        start = (curx, cury)
        goal = (goalx, goaly)
        return self.dict[(start, goal)]

