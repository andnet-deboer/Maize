import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import os
from colored import Fore, Back, Style
import time

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
    
 
    
    def updateMatrix(self,matrix):
        """ This a helper function to update the values of the matrix"""
        pass
         
    
    def display(self, path,showHistory):
        os.system('clear')

        matrix = np.array(self.maze)

        cmap = colors.ListedColormap(['green', 'gray', 'black', 'red', 'yellow'])
        norm = colors.BoundaryNorm([0, 1, 2, 3, 4], cmap.N)

        fig, ax = plt.subplots()
        im = ax.imshow(matrix, cmap=cmap, norm=norm)

        ax.set_xticks(np.arange(-0.5, len(self.maze[0]), 1))
        ax.set_yticks(np.arange(-0.5, len(self.maze), 1))
        ax.grid(which='major', linestyle='-', color='k', linewidth=1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_title("ROBOT MAIZE")

        plt.ion()
        plt.show()
        plt.draw()

        for i ,exploredCell in enumerate(path):
            if showHistory == False:
                prevCell = path[i-1]
                if prevCell != None:
                    self.maze[prevCell[0]][prevCell[1]] = 1 
                    matrix = np.array(self.maze)

            matrix[exploredCell[0]][exploredCell[1]] = 4
            im.set_data(matrix)
            plt.draw()
            plt.pause(0.5)

        plt.ioff()
        plt.show()


maze = Maze("maze.txt")
#maze.display([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 8), (1, 7), (1, 7), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (3, 8), (2, 8), (2, 9), (1, 9), (1, 9), (3, 9), (4, 9)])        
        