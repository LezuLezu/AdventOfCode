def getData():
    data = []
    # for line in open("2022/Day_07/TestData.txt"): 
    for line in open("2022/Day_07/Data.txt"): 
        data.append(line.rstrip())
    # print(data)
    return data

def getSizes(data):
    dirDict = {}
    dirList = []
    cd = ""
    for dataline in data:
        if '$ cd' in dataline and '..' not in dataline:
            dir = dataline.removeprefix('$ cd ')
            cd += dir
            if cd not in dirDict:
                dirDict[cd] = []
            dirList.append(dir)

        elif '$ cd' in dataline and '..' in dataline:
            cd = cd.removesuffix(dirList[len(dirList)-1])
            dirList.pop(len(dirList)-1)

        elif '$ cd' not in dataline and '$ ls' not in dataline:
            if 'dir' in dataline:
                dir = dataline.removeprefix('dir ')
                dirDict[cd+dir] = []
            else:
                size, name = dataline.split()
                dirDict[cd].append((int(size), name))

    total_size = {directory: 0 for directory in dirDict}

    for directory in dirDict:
        for item in dirDict[directory]:
            if type(item) == tuple:
                total_size[directory] += item[0]

    for key in total_size.keys():
        for directory in dirDict:
            if key in directory and key != directory:
                total_size[key] += total_size[directory]
    return total_size

def partOne(sizes):
    # print(sizes)
    total = 0
    for dirs in sizes:
        if sizes[dirs] <= 100000:
            # print(sizes[dirs])
            total += sizes[dirs]
    return total

def partTwo(sizes):
    emtySpace = 70000000 - max(sizes.values())
    spaceNeeded = 30000000 - emtySpace
    posibleDels = []
    for dirs in sizes:
        if sizes[dirs] >= spaceNeeded:
            posibleDels.append(sizes[dirs])
    return min(posibleDels)


def main():
    data = getData()
    sizes = getSizes(data)

    p1 = partOne(sizes)
    print("part one; Total size up to 100.000 per dir: %s" %(p1))

    p2 = partTwo(sizes)
    print("Part two; smallest dir total to delete: %s" %(p2))

main()