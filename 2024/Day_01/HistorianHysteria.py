def getData():
    data = []
    dataLines = []
    # with open("2024/Day_01/testData.txt", 'r') as f:
    with open("2024/Day_01/data.txt", 'r') as f:
        dataLines = f.read().split()
        # print(dataLines)
    line1 = dataLines[::2]
    line2 = dataLines[1::2]
    # print(line1)
    # print(line2)
    data = [line1, line2]
    data = [[int(x) for x in line] for line in data]
    return data
    
def findLowest(data):
    low_distance = 0
    low_sum = 0
    map1 = data[0]
    map1.sort()
    map2 = data[1]
    map2.sort()
    # print(map1)
    # print(map2)
    for i in range(len(map1)):
        low_distance = abs(map1[i] - map2[i])
        low_sum += low_distance

    return low_sum

def findSimilarity(data):
    count = 0
    map1 = data[0]
    map2 = data[1]
    for num in range(len(map1)):
        count += map1[num] * map2.count(map1[num])
    return count


def main():
    data = getData()
    # print(data)
    part1 = findLowest(data)
    print("Part one, lowCounter: %s"%(part1))
    part2 = findSimilarity(data)
    print("Part two, similarity score: %s "%(part2))


if __name__ == "__main__":
    main()