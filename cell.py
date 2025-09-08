class Cell:
    """ A class to manage each Cell of the Maze"""

    def __init__(self, row, col, state = 0):
        #Set the state of the cell
        self.state = state      #The cell will be initiliazed to be walled (Non-free)
        
        #Set the position in the maze of the cell:
        self.row = row
        self.col = col
    
    def __repr__(self):
        if(self.state == 0):
            return " ■ "
        elif(self.state == 1):
            return " □ "
        elif(self.state == 2):
            return " B "
        elif(self.state == 3):
            return " E "
        else: 
            return " X "

    def set_state(self,state):
        self.state = state          #Set the state to the input
    
    

        