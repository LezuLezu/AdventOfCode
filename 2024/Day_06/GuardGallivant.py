directions={
    'up' : [-1,0],
    'down':[1,0],
    'right':[0,1],
    'left':[0,-1]
}
visited = set()
visited2 = set()
grid = []
grid2 = []

def getData():
    data = []
    # with open("2024/Day_06/testData.txt", 'r') as f:
    with open("2024/Day_06/Data.txt", 'r') as f:

        for line in f:
            line=line.strip()
            data.append([])
            for element in line:
                data[-1].append(element)
    return data   

def findStart(grid):
    for line in range(len(grid)):
        for col in range(len(grid[0])-1):
            if grid[line][col] == "^":
                return [line, col]
            
def findPath(xCord, yCord, facing):
    while True:
        if not (0 <= xCord < len(grid) and 0 <= yCord < len(grid[0])):
            return
        if grid[xCord][yCord] == "#":
            if facing == "up":
                # turn right from facing upwards on the map -> right
                xCord +=  1
                facing = "right"
                continue
            if facing == "right":
                # turn right from facing right on the map -> down
                yCord -= 1
                facing = "down"
                continue
            if facing == "down":
                # turn right from facint down on the map -> left
                xCord -= 1
                facing = "left"
                continue
            if facing == "left":
                # turn right from facing left on the map -> up
                yCord += 1
                facing = "up"
                continue
        else:
            visited.add((xCord, yCord))
            grid[xCord][yCord] = "X"
            xMove, yMove = directions[facing]
            xCord += xMove
            yCord += yMove

def findVisited():
    visitedCounter = 0
    for row in grid:
        for pos in row:
            if pos == "X":
                visitedCounter += 1
    return visitedCounter

def findPathPart2(xCord, yCord, facing):
    path = {}
    while True:
        if not (0 <= xCord < len(grid2) and 0 <= yCord < len(grid2[0])):
            return
        if grid2[xCord][yCord] == "#":
            if facing == "up":
                # turn right from facing upwards on the map -> right
                xCord +=  1
                facing = "right"
                continue
            if facing == "right":
                # turn right from facing right on the map -> down
                yCord -= 1
                facing = "down"
                continue
            if facing == "down":
                # turn right from facint down on the map -> left
                xCord -= 1
                facing = "left"
                continue
            if facing == "left":
                # turn right from facing left on the map -> up
                yCord += 1
                facing = "up"
                continue
        else:
            path[str((xCord,yCord))]=path.get(str((xCord,yCord)),0)+1
            if path[str((xCord,yCord))] >= 6: # modified unitl no variance in ouput
                return True
            visited2.add((xCord, yCord))
            grid2[xCord][yCord] = "X"
            xMove, yMove = directions[facing]
            xCord += xMove
            yCord += yMove

def placeObstable(startX, startY):
    counter = 0
    for line in range(len(grid2)):
        for pos in range(len(grid2[0])-1):
            if grid2[line][pos] == "#" or  grid2[line][pos] == "^":
                continue
            grid2[line][pos] = "#"
            if findPathPart2(startX, startY, "up"):
                counter += 1
            grid2[line][pos] = "."
    return counter

    


def main():
    data = getData()
    # print(data)
    global grid 
    grid = data
    global grid2
    grid2 = data
    # print(grid)

    startLine, startCol = findStart(data)
    # print("Start position coords in grid: %s, %s"%(startLine, startCol))
    findPath(startLine, startCol, "up")
    visitGridCounter = findVisited()
    # print("Visted Grid pattern")
    # for line in grid:
    #     print(line)
    print("Part 1, visited %s positionsin the grid" %(visitGridCounter))
    findPathPart2(startLine, startCol, "up")
    part2 = placeObstable(startLine, startCol)
    print("Part 2, there are %s options to place obstacles"%(part2))

   
if __name__ == "__main__":
    main()