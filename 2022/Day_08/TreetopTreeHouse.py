import numpy as np

def getData():
    # with open("2022/Day_08/TestData.txt") as file:
    with open("2022/Day_08/Data.txt") as file:
        data = file.read().splitlines()
    # print(data)
    array = np.empty([len(data), len(data[0])])
    for j, item in enumerate(data):
        for i, number in enumerate(item):
            n = int(number)
            array[j, i] = n
    # print(array)
    return array

def getDirections(data, i, j):
    top = []
    bottom = []
    left = []
    right = []
    for trees in range(0, i):
        top.append(data[trees, j])
    for trees in range(i + 1, data.shape[0]):
        bottom.append(data[trees, j])
    for trees in range(0, j):
        left.append(data[i, trees])
    for trees in range(j + 1, data.shape[1]):
        right.append(data[i, trees])
    top.reverse()
    left.reverse()
    return top, bottom, left, right

def calculateVisibility(directions, maxHeight):
    score = 0
    for row in directions:
        vis = True
        for tree in row:
            if tree >= maxHeight:
                vis = False
                break
        if vis:
            score += 1
            break
    return score

       
def getVisTrees(data):
    visibleTrees = 0
    # Edges of the grid are always visible
    visibleTrees = data.shape[0]*2 + data.shape[1] * 2 - 4
    collum, row = data.shape
    for i in range(1, collum - 1):
        for j in range(1, row - 1):
            currentIndex = data[i, j]
            directions = getDirections(data, i, j)
            visibleTrees += calculateVisibility(directions, currentIndex)
    return visibleTrees

def getTreeScore(data):
    treeScore = []
    collum, row = data.shape
    for i in range(1, collum - 1):
        for j in range(1, row - 1):
            currentIndex = data[i, j]
            directions = getDirections(data, i, j)
            treeScore.append(calcScore(data, directions, i, j))
    # print(treeScore)
    return max(treeScore)
    
def calcScore(data, directions, i, j):
    treeScore = 1
    for line in directions:
        val = calcLineVis(data, line, i, j)
        treeScore *= val
    return treeScore

def calcLineVis(data, line, i, j):
    score = 0
    currentVal = data[i, j]
    for tree in line:
        score += 1
        if tree >= currentVal:
            break
    return score


def main():
    data = getData()

    visibleTrees = getVisTrees(data)
    print("Part One: Visible amount of trees from the outside %s"%(visibleTrees))

    treeScore = getTreeScore(data)
    print("Part Two: Best Scoring Tree has %s points" %(treeScore))

main()