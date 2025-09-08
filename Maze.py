import numpy as np


class Maze():

    def __init__(self):
        self.maze = None
        self.wallCell =[]
        self.freeCell = []
        self.start = None
        self.goal = None


    def load(self,filename):

        with open(filename, 'r') as f:
            lines = f.readlines()

        maze = []

        for line in lines:
            row = None