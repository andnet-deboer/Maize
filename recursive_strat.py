import maze_manual
def solve_maze(maze, r, c, path, history):
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False

    if maze[r][c] == 2 or maze[r][c] == -1:
        return False

    path.append((r, c))
    history.append((r, c))

    if maze[r][c] == 3:
            return True

    maze[r][c] = -1

    if (solve_maze(maze, r-1, c, path, history) or # up
        solve_maze(maze, r, c+1, path, history) or # right
        solve_maze(maze, r+1, c, path, history) or # down
        solve_maze(maze, r, c-1, path, history)): # left
        return True

    history.append(path.pop())
    history.append(path[-1])
    return False

maze_obj = maze_manual.Maze("datafile.txt")
print(f"Maze: {maze_obj.maze}")
#maze_obj = [[0, 1, 1, 1, 2], [2, 2, 1, 2, 2], [2, 2, 1, 1, 3]]

path = []
history = []

maze = maze_manual.Maze("datafile.txt")

if solve_maze(maze_obj.maze, maze_obj.start[0],maze_obj.start[1], path, history):
    #print("Path:", path)
    #print ("History:", history)
    maze.display(history,False)
else:
    print("No path found")