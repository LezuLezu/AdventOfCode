def getData():
    data = []
    # with open("2022/Day_09/TestData.txt") as file:
    # with open("2022/Day_09/TestData_2.txt") as file:
    with open("2022/Day_09/Data.txt") as file:
        data = [line.strip().split(" ") for line in file]
    # print(data)
    return data

def tailTracker(data, amountOfKnots):
    ropeGrid = [(10, 10)] * amountOfKnots
    # print(ropeGrid)
    tailHasVisited = set()
    tailHasVisited.add(ropeGrid[-1])        #start position

    # directions for the head knot
    for (direction, steps) in data:                         # loop trough data lines
        for step in range(int(steps)):                      # loop trough grid amount of steps (data[1])
                                                            # for each step make a move
            if direction == "L":
                ropeGrid[0] = (ropeGrid[0][0], ropeGrid[0][1] - 1)

            elif direction == "R":
                ropeGrid[0] = (ropeGrid[0][0], ropeGrid[0][1] + 1)

            elif direction == "U":
                ropeGrid[0] = (ropeGrid[0][0]  - 1, ropeGrid[0][1])
            
            elif direction == "D":
                ropeGrid[0] = (ropeGrid[0][0]  + 1, ropeGrid[0][1])

        # where the tail knot will follow
            for knot in range(1, len(ropeGrid)):
                rowDirection = ropeGrid[knot - 1][0] - ropeGrid[knot][0]
                colDirection = ropeGrid[knot - 1][1] - ropeGrid[knot][1]

                if rowDirection != 0:
                    rowDirection -= 1 if rowDirection > 0 else -1
                if colDirection != 0:
                    colDirection -= 1 if colDirection > 0 else -1
                if rowDirection or colDirection:
                    ropeGrid[knot] = (ropeGrid[knot - 1][0] - rowDirection, ropeGrid[knot - 1] [1] - colDirection)

            tailHasVisited.add(ropeGrid[-1])
    return len(tailHasVisited)



def main():
    data = getData()

    p1 = tailTracker(data, 2)
    print("Part One: tail has visited %s positions at least once" %(p1))

    p2 = tailTracker(data, 10)
    print("Part two: tail has visited %s positions at least once" %(p2))

main()
