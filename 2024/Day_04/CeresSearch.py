import numpy as np

def getData():
    data = []
    dataLines = []
    # with open("2024/Day_04/testData.txt", 'r') as f:
    with open("2024/Day_04/data.txt", 'r') as f:
        data = f.read().split()   
    return data

def findXMAS(data):
    xmasCounter = 0
    rows = len(data)
    cols = len(data[0])
    for row in range(rows):
        # print(row)
        for col in range(cols):
            # print(col)
            if(data[row][col]) == "X":
                # North - up
                if row >= 3:
                    if data[row-1][col] + data[row-2][col] + data[row-3][col] == "MAS":
                        xmasCounter += 1
                # NorthEast - diagnal right upwards
                if row >= 3 and col <= cols-4:
                    if data[row-1][col+1] + data[row-2][col+2] + data[row-3][col+3] == "MAS":
                        xmasCounter += 1
                # East - left
                if col <= cols-4:
                    if data[row][col+1] + data[row][col+2] + data[row][col+3] == "MAS":
                        xmasCounter += 1
                # SoutEast - diagnal right downwards
                if row <= rows-4 and col <= cols -4:
                    if data[row+1][col+1] + data[row+2][col+2] + data[row+3][col+3] == "MAS":
                        xmasCounter += 1
                # South - down
                if row <= rows-4:
                    if data[row+1][col] + data[row+2][col] + data[row+3][col] == "MAS":
                        xmasCounter += 1
                # SouthWest - diagnal left downwards
                if row <= rows-4 and col >= 3:
                    if data[row+1][col-1] + data[row+2][col-2] + data[row+3][col-3] == "MAS":
                        xmasCounter += 1
                # West - left
                if col >= 3:
                    if data[row][col-1] + data[row][col-2] + data[row][col-3] == "MAS":
                        xmasCounter += 1
                # NorhtWest - diagnal right upwards
                if row >= 3 and col >= 3:
                    if data[row-1][col-1] + data[row-2][col-2] + data[row-3][col-3] == "MAS":
                        xmasCounter += 1
    return xmasCounter

def findMAS(data):
    masCounter = 0
    rows = len(data)
    cols = len(data[0])
    for row in range(1, rows):
        for col in range(1, cols):
            if(data[row][col]) == "A" and row < rows-1 and col < cols-1:
            # Check corners 
                # top righ  +   left bottom
                if data[row-1][col+1] == "M" and data[row+1][col-1] == "S":
                    # top left + righ bottom
                    if data[row-1][col-1] == "M" and data[row+1][col+1] == "S":
                        masCounter += 1
                        # top left + bottom right
                    elif data[row-1][col-1] == "S" and data[row+1][col+1] == "M":
                            masCounter += 1
                # top right + bottom left
                elif data[row-1][col+1] == "S" and data[row+1][col-1] == "M":
                    # top left + bottom right
                    if data[row-1][col-1] == "M" and data[row+1][col+1] == "S":
                        masCounter += 1
                        # top left + bottom right
                    elif data[row-1][col-1] == "S" and data[row+1][col+1] == "M":
                        masCounter += 1
    return masCounter



def main():
    data = getData()
    # print(data)
    part1 = findXMAS(data)
    print("Part one, find XMAS in the grid, counter: %s"%(part1))
    part2 = findMAS(data)
    print("Part two, find the X-MAS in the grid, counter: %s" %(part2))
   
if __name__ == "__main__":
    main()