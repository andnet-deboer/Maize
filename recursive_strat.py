import maze_manual
def solve_maze(maze, r, c, path):
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False

    if maze[r][c] == 2 or maze[r][c] == -1:
        return False

    path.append((r, c))

    if maze[r][c] == 3:
        return True

    maze[r][c] = -1

    if (solve_maze(maze, r-1, c, path) or # up
        solve_maze(maze, r, c+1, path) or # right
        solve_maze(maze, r+1, c, path) or # down
        solve_maze(maze, r, c-1, path)): # left
        return True

    path.pop()
    return False

maze_obj = maze_manual.Maze("maze.txt")
print(f"Maze: {maze_obj.maze}")


path = []
if solve_maze(maze_obj.maze, 0, 0, path):
    print("Path:", path)
else:
    print("No path found")