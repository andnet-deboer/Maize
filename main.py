
from maze_manual import Maze

import recursive_strat
import maze_manual


def main():
    maze_obj = maze_manual.Maze("MazeFiles/datafile.txt")

    path = []
    history = []

    maze = maze_manual.Maze("MazeFiles/datafile.txt")

    if recursive_strat.solve_maze(maze_obj.maze, maze_obj.start[0],maze_obj.start[1], path, history):
        maze.display(path)
    else:
        print("No path found")


if __name__ == '__main__':
    main()
