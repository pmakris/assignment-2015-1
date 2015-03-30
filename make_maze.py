
import random
import sys

class Cell:
    #Variable to check if a cell is visited
    Visited = False
    def __init__(self,bool):
        self.Visited = bool


argnum = len(sys.argv)


#Check for correct number of arguments
if argnum != 6:
    print("Wrong call of make_maze, it should be: make_maze.py <n> <start_x> <start_y> <seed> <output_file>")
    sys.exit(1)
else:
    n = int(str(sys.argv[1]))
    start_x = int(str(sys.argv[2]))
    start_y = int(str(sys.argv[3]))
    rand_seed = int(str(sys.argv[4]))
    output_file = str(sys.argv[5])

#Check for correct range of start_x and start_y
if start_x > n or start_y > n or n > 30:
    print("ERROR: 0 <= start_x < n and 0 <= start_y < n and n <= 30")
    sys.exit(1)
else:

    random.seed(rand_seed)
    height = n
    width = n
#fuction for generating the Maze, n x n
def MazeGenerator(width,height):
    # 2D Maze list
    Maze = [Cell]*width
    for i in range(width):
        Maze[i] = [Cell]*height

    #Stack for holding coordinates of cells
    CellStack = []

    #Total number of cells
    TotalNumofCells = width*height

    #How many Cells is checked
    CellsChecked = 0

    # Coordinates of starting cell
    StartingCell = [start_x, start_y]
    # StartingCell = [0, 3] #test

    #Variables for possible directions
    Up = [0, 1]
    Right = [1, 0]
    Left = [-1, 0]
    Down = [0, -1]

    #Fill Maze with Cells, n x n
    for i in range(0,height):
        for j in range(0,width):
            Maze[i][j] = Cell(False)
            # print("Cell created at coordinates: " +str(i)+","+str(j))

    #Function for setting a cell as visited and add it to the stack
    def AddCell(CellList):
        Maze[CellList[0]][CellList[1]].Visited = True
        CellStack.append(CellList)

    #Check for possible direction
    def CheckCell(direction):

        x = direction[0]+CellStack[-1][0]
        y = direction[1]+CellStack[-1][1]

        if x<0 or y<0:
            print("Error:Negative value")
            # print("i cannot go to "+str(x)+" "+str(y)+" with direction "+str(direction[0])+" "+str(direction[1]))
            return 0
        elif x>=width or y>=height:
            print("Error: Out of bounds "+str(x)+" "+str(y))
            # print("i cannot go to "+str(x)+" "+str(y)+" with direction "+str(direction[0])+" "+str(direction[1]))
            return 0
        elif Maze[x][y].Visited == True:
            return  0
        else:
            # print("i can go to "+str(x)+" "+str(y)+" with direction "+str(direction[0])+" "+str(direction[1]))
            return direction

    #Find the neighbors of Cell
    def FindNeighbors(Cell):

        Neighbors = []
        GoUp = CheckCell(Up)
        GoDown = CheckCell(Down)
        GoLeft = CheckCell(Left)
        GoRight = CheckCell(Right)
        if GoUp:
            Neighbors.append(Up)
        if GoDown:
            Neighbors.append(Down)
        if GoRight:
            Neighbors.append(Right)
        if GoLeft:
            Neighbors.append(Left)
        # print(Neighbors)
        return Neighbors

    #Main funcionality of program
    AddCell(StartingCell)
    while CellsChecked < TotalNumofCells and len(CellStack)>0:
        #Find the neighbors of a cell
        CellNeighbors = FindNeighbors(StartingCell)
        if len(CellNeighbors) > 0:
            #Choose a random neighbor to go
            NeighborChoice=CellNeighbors[random.randrange(0,len(CellNeighbors))]
            CellNeighbor = [CellStack[-1][0]+NeighborChoice[0],CellStack[-1][1]+NeighborChoice[1]]
            AddCell(CellNeighbor)
            CellsChecked += 1
        else:
            break
        print("Cell Stack: "+str(CellStack))

    # print(len(CellStack))
    #Convert Celstack to tuple and print results to file
    CellStack = [tuple(x) for x in CellStack]
    fo = open(output_file, "w")
    for i in range(0,len(CellStack)):
        print(', '.join([str(CellStack[i]), str(CellStack[i+1])]), file=fo)
    fo.close()

MazeGenerator(n, n)