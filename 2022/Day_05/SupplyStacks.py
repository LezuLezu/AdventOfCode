
testStacks = {
    "1" : ["Z", "N"],
    "2" : ["M", "C", "D"],
    "3" : ["P"]
}

stacksPrime = {
    "1" : ["V", "C", "D", "R", "Z", "G", "B", "W"],
    "2" : ["G", "W", "F", "C", "B", "S", "T", "V"],
    "3" : ["C", "B", "S", "N", "W"],
    "4" : ["Q", "G", "M", "N", "J", "V", "C", "P"],
    "5" : ["T", "S", "L", "F", "D", "H", "B"],
    "6" : ["J", "V", "T", "W", "M", "N"],
    "7" : ["P", "F", "L", "C", "S", "T", "G"],
    "8" : ["B", "D", "Z"],
    "9" : ["M", "N", "Z", "W"],
}

def getMoves():
    moves = []
    # for line in open("2022/Day_05/TestData.txt"):
    for line in open("2022/Day_05/Data.txt"):
        if line.startswith("move"):
            line = line.split()
            # print(line)
            newLine = [line[1], line[3], line[-1]]
            # print(newLine)
            moves.append(newLine)
    # print(moves)
    return moves

def getTopCrates(moves):
    stacks = stacksPrime.copy()
    # for line in moves:
    #     # print(line)
    #     for crates in range(int(line[0])):
    #         # print(crates)
    #         testStacks[line[2]].append(testStacks[line[1]].pop())
    #     # print(testStacks)
    # topItems = [testStacks[key][-1] for key in testStacks]
    for line in moves:
        for crates in range(int(line[0])):
            stacks[line[2]].append(stacks[line[1]].pop())
    topItems = [stacks[key][-1] for key in stacks]
    # print(topItems)
    # print(testStacks)
    return topItems

def getTopCratesFor9001(moves):
    stacks = stacksPrime.copy()
    topItems = []
    for line in moves:
        # print(line[0])
        crateToMove = []
        for crates in range(int(line[0])):
            crateToMove.append(stacks[line[1]].pop())
        stacks[line[2]].append(crateToMove[-1])
    topItems = [stacks[key][-1] for key in stacks]
    print(topItems)
    return topItems
        
def main():
    moves = getMoves()
    p1 = getTopCrates(moves)
    print("Part one, top Stacks %s" %(''.join(p1)))
    p2 = getTopCratesFor9001(moves)
    print("Part two, top Stacks %s" %(''.join(p2)))

main()

