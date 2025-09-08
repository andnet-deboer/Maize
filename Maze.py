import numpy as np
import matplotlib as plt
import os
from colored import Fore, Back, Style

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
        return maze    
    
    def display(self,path):
        os.system('clear')
        for cell in self.maze:
            if cell == 0:
                    Fore.red
                    print(cell)
            elif cell == 1:
                    Fore.blue
                    print(cell)
            elif cell == 2:
                    Fore.black
                    print(cell)
            elif cell == 3:
                    Fore.green
                    print(cell)

maze = Maze("maze.txt")
maze.display((0,0),(0,1))
        
        