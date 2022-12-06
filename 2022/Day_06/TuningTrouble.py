from itertools import count

def getData():
    # data = open("2022/Day_06/TestData.txt", "r").read()
    data = open("2022/Day_06/Data.txt", "r").read()
    return data

def findMarker(data, length):
    # length  = 4
    index = next(i for i in count() if len(set(data[i - length : i])) == length)

    # print(index)
    return index

def main():
    data = getData()
    # print(data)
    p1 = findMarker(data, 4)
    print("Part one, index of starter marker is %s" %(p1))
    p2 = findMarker(data, 14)
    print("Part tow, index of starter marker is %s" %(p2))

main()