import Viewer

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ START,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
        [EMPTY, EMPTY,  WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  WALL, EMPTY,  WALL, EMPTY,  WALL, EMPTY, WALL],
        [ EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, EMPTY, EMPTY, WALL],
        [ EMPTY,  WALL, EMPTY,  WALL,  WALL, EMPTY, EMPTY,  WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL,  WALL, EMPTY,  END],
        [ WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
    ]
                    
    Viewer.view(grid)

    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    Row = 1
    Col = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(Row) + ", " + str(Col) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            Row -= 1
            
        elif direction == EAST:
            Col += 1
                
        elif direction == SOUTH:
            Row += 1
                
        elif direction == WEST:
            Col -= 1
        
        else:
            print("You have no idea where you're going.") # Invalid direction.
        
        if (Row < 0 or Col < 0 
                        or Row >= len(grid) 
                        or Col >= len(grid[Row])):
            done = True
            print("You fall into the chasm of doom.") # Out of bounds.
            
        else:
            cell =  grid[Row][Col]
            if cell == EMPTY:
                grid[Row][Col] = VISITED
                
            elif cell == WALL: 
                done = True
                print("You stumble blindly into a solid concrete wall.") # Hit wall.

            elif cell == END:
                done = True
                solved = True
                print("SOLVED!") # Solved.
                
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("You have failed to escape. Future archeologists gaze upon your remains in bafflement.") # Did not reach the end.

    Viewer.view(grid)
