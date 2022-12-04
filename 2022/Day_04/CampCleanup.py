
def getData():
    data = []
    newList = []
    # for line in open("2022/Day_04/TestData.txt"):    
    for line in open("2022/Day_04/Data.txt"):

        line = line.rstrip().split(",")
        # print(line)
        newList.append([item.split("-") for item in line])
    data = [[[int(num) for num in item]for item in line]for line in newList]
    # print(data)
    return(data)

def getPairOverLapCount(data):
    count = 0
    for line in data:
        # print(line)
        firstElf = line[0]
        secondElf = line[1]
        # print(firstElf)
        if firstElf[0] <= secondElf[0] and firstElf[1] >= secondElf[1]:
            count += 1
        elif secondElf[0] <= firstElf[0] and secondElf[1] >= firstElf[1]:
            count += 1
    return count

def getOverLapCount(data):
    count = 0
    for line in data:
        firstElf = line[0]
        secondElf = line[1]
        if firstElf[1] >= secondElf[0] and firstElf[0] <= secondElf[1]:
            count += 1
    return count

def main():

    data = getData()
    p1 = getPairOverLapCount(data)
    print("Part one: Pair overlap is %s" %(p1))
    p2 = getOverLapCount(data)
    print("Part one: Total overlap is %s" %(p2))

main()