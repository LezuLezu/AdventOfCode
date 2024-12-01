def getData():
    # with open("2022/Day_10/TestDataLarge.txt") as file:
    # with open("2022/Day_10/TestData.txt") as file:
    with open("2022/Day_10/Data.txt") as file:
        data = [line.strip().split(" ") for line in file]     
    for line in data:
        if len(line) == 2:
            line[1] = int(line[1])
            
    # print(data)
    return data

def getSignalStrength(data):
    cycleCount = 1
    cycleCountStrenghtList = [20, 60, 100, 140, 180, 220]
    sigalStrengthList = []
    register = 1

    for line in data:
        if line[0] == "noop":
            cycleCount += 1
        elif line[0] == "addx":
            cycleCount += 1
            if cycleCount in cycleCountStrenghtList:
                # print(cycleCount * register)
                sigalStrengthList.append(cycleCount * register)
            register += line[1]
            cycleCount += 1
        if cycleCount in cycleCountStrenghtList:
                # print(cycleCount * register)
                sigalStrengthList.append(cycleCount * register)
    return sum(sigalStrengthList)

def fillGrid(grid, cycleCount, register):
    # print(cycleCount)
    # print(register)
    if abs((cycleCount % 40) - register) <= 1:
        # print("in grid draw")
        grid[max(0, cycleCount // 40)][min(40, cycleCount % 40)] = "#"
    return grid

def grid(data):
    cycleCount = 0
    register = 1
    gridWith = 40
    gridHeight = 6
    grid = [["." for x in range(gridWith)] for y in range(gridHeight)]

    for line in data:
        grid = fillGrid(grid, cycleCount, register)
        if line[0] == "noop":
            cycleCount += 1
        elif line[0] == "addx":
            cycleCount += 1
            grid = fillGrid(grid, cycleCount, register)
            register += line[1]
            cycleCount += 1
        grid = fillGrid(grid, cycleCount, register)
    return grid

def main():
    data = getData()

    p1 = getSignalStrength(data)
    print("Part One: Sum of six signal Strengths is %s" %(p1))

    p2 = grid(data)
    print('Part 2\n')
    for line in p2:
        print(''.join(line))

main()