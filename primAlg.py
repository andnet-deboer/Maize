from cell import Cell
import numpy as np
import random

def print_maze(maze):
    #Determine the size of the maze:
    rows = len(maze)
    columns = len(maze[0])

    for r in range(rows):
        for c in range(columns):
            print(maze[r][c].__repr__(), end = "")
        print("\n")

def print_maze_num(maze):
    #Determine the size of the maze:
    rows = len(maze)
    columns = len(maze[0])

    for r in range(rows):
        for c in range(columns):
            print(f"{maze[r][c].state} ", end = "")
        print("\n")

def index_exists(matrix, row, col):
    return (
        0 <= row < len(matrix) and
        0 <= col < len(matrix[row])
    )

def adj_one(matrix, test):
    rows = len(matrix)
    cols = len(matrix[0])
    numFree = 0
    oneFree = None

    #Determine how many are adjactent to the test Cell:
    if(0 <= test.row - 1 < rows and matrix[test.row - 1][test.col].state >= 1):  # Up
        numFree += 1
        oneFree = matrix[test.row - 1][test.col]
    if(0 <= test.row + 1 < rows and matrix[test.row + 1][test.col].state >= 1):  # Dowm
        numFree += 1
        oneFree = matrix[test.row + 1][test.col]
    if(0 <= test.col - 1 < cols and matrix[test.row][test.col - 1].state >= 1):  # Left
        numFree += 1
        oneFree = matrix[test.row][test.col - 1]
    if(0 <= test.col + 1 < cols and matrix[test.row][test.col + 1].state >= 1):  # Right
        numFree += 1
        oneFree = matrix[test.row][test.col + 1]

    if(numFree == 1):
        return oneFree
    else:
        return None

def dir_W(matrix,W,F):
    rows = len(matrix)
    cols = len(matrix[0])
    DIR = 0         #0-North, 1-South, 2-East, 3-West

    if(index_exists(matrix, W.row -1, W.col) and matrix[W.row - 1][W.col] == F):  # Up
        DIR = 1 #South
    if(index_exists(matrix, W.row + 1, W.col) and matrix[W.row + 1][W.col] == F):  # Dowm
        DIR = 0 #North
    if(index_exists(matrix, W.row, W.col - 1) and matrix[W.row][W.col - 1] == F):  # Left
        DIR = 3 #West
    if(index_exists(matrix, W.row, W.col + 1) and matrix[W.row][W.col + 1] == F):  # Right
        DIR = 2 #East
    return DIR

def ret_A(matrix,W,DIR):    
    rows = len(matrix)
    cols = len(matrix[0])
    A = None

    if(DIR == 0 and index_exists(matrix, W.row - 1, W.col)):    #Return the cell (A) north of W if it exists
        A = matrix[W.row - 1][W.col]
    if(DIR == 1 and index_exists(matrix, W.row + 1, W.col)):    #Return the cell (A) south of W if it exists
        A = matrix[W.row + 1][W.col]
    if(DIR == 2 and index_exists(matrix, W.row, W.col - 1)):    #Return the cell (A) East of W if it exists
        A = matrix[W.row][W.col - 1]
    if(DIR == 3 and index_exists(matrix, W.row, W.col + 1)):    #Return the cell (A) West of W if it exists
        A = matrix[W.row][W.col + 1]
    return A

def add_walls(matrix, walls, freeCell):
    #Find the index of the freeCell in the matrix: 
    id_row = 0
    id_col = 0
    for i,row in enumerate(matrix):
        for j, cell in enumerate(row): 
            if cell == freeCell:
                id_row = i
                id_col = j

    #Check to see if the neighbors exist:
    if index_exists(matrix, id_row - 1, id_col):  # Up
        walls.append(matrix[id_row - 1][id_col])
    if index_exists(matrix, id_row + 1, id_col):  # Down
        walls.append(matrix[id_row + 1][id_col])
    if index_exists(matrix, id_row, id_col - 1):  # Left
        walls.append(matrix[id_row][id_col - 1])
    if index_exists(matrix, id_row, id_col + 1):  # Right
        walls.append(matrix[id_row][id_col + 1])
    return walls


def prim_alg():
    print("We will determine what size rectangular maze would you like to create (M x N): ")
    M = int(input("Please input the horizontal dimension:"))
    N = int(input("Please input the vertical dimension:"))
    
    #Create Cells for each row in the matrix:
    maze = [[Cell(row, col) for col in range(M)] for row in range(N)]

    #Implement the Prim Algorithm:
    
    #Randomly choose and X and Y position:
    rand_row = random.randint(0, M-1)   #Generates a random integer between 0 and M-1
    rand_col = random.randint(0,N-1)    #Generates a random integer between 0 and N-1

    #Change the state of the randomly selected Cell (Q):
    Q = maze[rand_row][rand_col]
    Q.state = 2

    #Add Cell Q's neighbors to a Wall list: 
    wall_list = []
    add_walls(maze,wall_list,Q)

    #print(f"The Row and Col of Q is {Q.row} and {Q.col}")
    #print_maze(maze)


    #While the wall list is not empy recursively build the maze:
    while len(wall_list) >= 1:
        W = wall_list[random.randint(0, len(wall_list) - 1)]   #Generates a random integer between 0 and # of walls in list

        #print(f"The length of wall_list is {len(wall_list)}")
        #print(f"The Row and Col of W is {W.row} and {W.col}")

        #print_maze(maze)

        #Determine F if there is one cell free next to W
        F = None
        if adj_one(maze,W) is not None: 
            F = adj_one(maze,W)

            #print(f"The Row and Col of W is {F.row} and {F.col}")
            #Determine the Direction of W to F and return A:
            dir = dir_W(maze,W,F)
            #print(f"The direction of f is {dir}")
            A = ret_A(maze,W, dir)

            #Make W and A free:
            W.state = 1
            if(A is not None):
                A.state = 1
                #Add the Walls of A to the wall list
                wall_list = add_walls(maze,wall_list,A)
        
        if len(wall_list) == 1:
            W.state = 3

        #Remove W from the Wall_list
        wall_list.remove(W)
    
    return maze

def main(): 
    #Generate a maze:
    maze = prim_alg()

    #Print the maze:
    print_maze(maze)

    #Export the maze as a .txt file:
    #print_maze_num(maze)


if __name__ == '__main__':
    main()