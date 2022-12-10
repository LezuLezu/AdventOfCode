def getData():
    # with open("2022/Day_10/TestDataLarge.txt") as file:
    # with open("2022/Day_10/TestData.txt") as file:
    with open("2022/Day_10/Data.txt") as file:
        data = [line.strip().split(" ") for line in file]     
    for line in data:
        if len(line) == 2:
            # print(line)
            if line[1].startswith("-"):
                line[1] = ["-", int(line[1][1:])]
            else:
                line[1] = ["+", int(line[1])]
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
        if line[0] == "addx":
            cycleCount += 1
            if cycleCount in cycleCountStrenghtList:
                # print(cycleCount * register)
                sigalStrengthList.append(cycleCount * register)
            if line[1][0] == "+":
                register += line[1][1]
                cycleCount += 1
            if line[1][0] == "-":
                register -= line[1][1]
                cycleCount += 1
        if cycleCount in cycleCountStrenghtList:
            sigalStrengthList.append(cycleCount * register)


    # print(sigalStrengthList)
    # print(sum(sigalStrengthList))
    return sum(sigalStrengthList)

# def grid(data):


            


def main():
    data = getData()
    # print(data)
    p1 = getSignalStrength(data)
    print("Part One: Sum of six signal Strengths is %s" %(p1))
main()