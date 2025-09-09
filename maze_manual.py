import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import os
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
    
    def display(self, path):
        """ This is a function to display the """
        matrix = np.array(self.maze)  

        #Create a set of colors to display on map
        cmap = colors.ListedColormap(['green', 'gray', 'black', 'red', 'yellow'])
        norm = colors.BoundaryNorm([0, 1, 2, 3, 4, 5], cmap.N)

        #show image with color map and then retrive the current axis
        im = plt.imshow(matrix, cmap=cmap, norm=norm) 
        ax = plt.gca() 
        ax.set_title("ROBOT MAIZE")
        
        #draw plot
        plt.draw()
   
        # For explored cells go back and hide cell colors to match free cell color
        for exploredCell in path:
            matrix = np.array(self.maze)
            r, c = exploredCell
            #Color visited paths
            if self.maze[r][c] not in (0,3):
                matrix[r][c] = 4 
            #update matrix
            im.set_data(matrix)

            #redraw plot
            plt.draw()
            plt.pause(0.1)
