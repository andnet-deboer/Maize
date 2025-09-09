
from maze_manual import Maze

import recursive_strat
import maze_manual
import os


def main():

    
    maze_obj = maze_manual.Maze("MazeFiles/data50x50.txt")

    path = []
    history = []

    maze = maze_manual.Maze("MazeFiles/data50x50.txt")

    hist = int(input("\nEnter 0 for final path enter 1 to visualize full exploration: "))

    if recursive_strat.solve_maze(maze_obj.maze, maze_obj.start[0],maze_obj.start[1], path, history):
        if hist == 0:
            maze.display(path)
        else:
            maze.display(history)
    else:
        print("No path found")


if __name__ == '__main__':
    main()
