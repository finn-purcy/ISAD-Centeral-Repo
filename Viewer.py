import Maze1

def view(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j] == Maze1.EMPTY:
                print("  ", end = "")

            elif grid[i][j] == Maze1.WALL:
                print("##", end = "")

            elif grid[i][j] == Maze1.START:
                print("^^", end = "")

            elif grid[i][j] == Maze1.END:
                print("$$", end = "")

            elif grid[i][j] == Maze1.VISITED:
                print("..", end = "")

            else:
                raise AssertionError

        print()

