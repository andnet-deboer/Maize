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
    
    def color(self, value):
        color = None
        match value:
             case 0:
                color = f'{Fore.green}'
             case 1:
                color = f'{Fore.white}'
             case 2:
                color = f'{Fore.black}'
             case 3:
                color = f'{Fore.red}'
             case -1:
                color = f'{Fore.yellow}'
        return color
    
    def updateMatrix(self,matrix):
        """ This a helper function to update the values of the matrix"""
        pass
         
    
    def display(self,path):
        os.system('clear')
        
        matrix = self.maze
        ########### Direct citation (3)  ########
        cmap = colors.ListedColormap(['yellow','green','gray','black','white','red',])
        fig, ax = plt.subplots()
        norm = colors.BoundaryNorm([-1, 0, 1, 2, 3, 4,], cmap.N)
        
        for exploredCell in path:
            self.maze[exploredCell[0]][exploredCell[1]] = -1

            ax.imshow(matrix, cmap=cmap, norm=colors.BoundaryNorm([-1, 0, 1, 2, 3, 4], cmap.N))

            # draw gridlines
            ax.set_xticks(np.arange(-0.5, len(self.maze[0]), 1))
            ax.set_yticks(np.arange(-0.5, len(self.maze), 1))
            ax.grid(which='major', linestyle='-', color='k', linewidth=1)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.set_title("ROBOT MAIZE")
            time.sleep(1)
            plt.show()
   


maze = Maze("maze.txt")
maze.display([(0,0),(0,1),(0,2)])
        
        