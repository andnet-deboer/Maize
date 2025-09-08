from Maze import Maze

def solve_maze(maze, r, c, path):
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False

    if maze[r][c] == 2 or maze[r][c] == -1:
        return False

    path.append((r, c))

    if maze[r][c] == 3:
        return True

    maze[r][c] = -1

    if (solve_maze(maze, r-1, c, path) or
        solve_maze(maze, r, c+1, path) or
        solve_maze(maze, r+1, c, path) or
        solve_maze(maze, r, c-1, path)):
        return True
    
    path.pop()
    return False

if __name__ == "__main__":
    myMaze = Maze("maze.txt") 
    maze = myMaze.maze.tolist()

    path = []
    if solve_maze(maze, 0, 0, path):
        print("Start:", myMaze.start)
    else:
        print("No path found")
