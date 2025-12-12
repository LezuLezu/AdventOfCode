def getData():  
    # with open("2024/Day_02/testData.txt", "r") as file:
    with open("2024/Day_02/Data.txt", "r") as file:
        data = file.read().split("\n")
    for i in range(len(data)):
        data[i] = data[i].split()
    data = [[int(x) for x in line] for line in data]
    return data

def findSafe(data):
    # alterered to safecheck function for general use in part 1 and 2
    safeCounter = 0
    for level in data:
        if safeCheck(level):
            safeCounter += 1
    return safeCounter

def safeCheck(line):
    safe1 = all(i < j and 1 <= (j - i) <= 3 for i, j in zip(line, line[1:]))
    safe2 = all(i > j and 1<= (i - j) <= 3 for i, j in zip(line, line[1:]))
    return safe1 or safe2

def findSafeWithDampener(data):
    safeList = []
    unsafeList = []
    for level in data:
        if safeCheck(level):
            safeList.append(level)
        else:
            unsafeList.append(level)
    for line in unsafeList:
        for num in range(len(line)):
            modifiedLine = line[:num] + line[num+1:]
            if safeCheck(modifiedLine):
                safeList.append(modifiedLine)
                break
    return len(safeList)
    
def main():
    data = getData()
    # print(data)
    part1 = findSafe(data)
    print("Part one, safeCounter: %s"%(part1))
    part2 = findSafeWithDampener(data)
    print("Part two, safeCounter with dampener: %s"%(part2))

if __name__ == "__main__":
    main()