import numpy as np

class Maze():

    def __init__(self,filename):
        self.wallCell =[]
        self.freeCell = []
        self.start = None
        self.goal = None
        self.maze = self.load(filename)


    def load(self,filename):

        with open(filename, 'r') as f:
            lines = f.readlines()
        maze = []

        for i,line in enumerate(lines):
            row = list(map(int,line.strip().split()))
            maze.append(row)
            for j, cell in enumerate(row):
                if cell == 0:
                    self.start = (i,j)
                elif cell == 1:
                    self.freeCell.append((i,j))
                elif cell == 2:
                    self.wallCell.append((i,j))
                elif cell == 3:
                    self.goal = (i,j)
        
        return np.array(maze)
    
myMaze = Maze("maze.txt")