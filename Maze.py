import numpy as np


class Maze():

    def __init__(self,filename):
        self.maze = self.load(filename)
        self.wallCell =[]
        self.freeCell = []
        self.start = None
        self.goal = None


    def load(self,filename):

        with open(filename, 'r') as f:
            lines = f.readlines()
        maze = []

        for line in lines:
            row = list(map(int,line.strip().split()))
            maze.append(row)
        
        return np.array(maze)