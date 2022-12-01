import re
from re import escape

def getData():
    data = []
    with open("2015/Day_08/Data.txt", 'r') as f:
    # with open("2015/Day_08/testdata.txt", 'r') as f:
        dataF = f.readlines()
    for line in dataF:
        line = line.strip("\n")
        data.append(line)
    # print(data)
    return data

def partOne(data):
    length = 0
    memory = 0
    for line in data:
        length += len(line)
        memory += len(eval(line))
    print(length, memory)
    total = length - memory
    return total, length, memory

def partTwo(data):
    length = 0
    encodeLenght = 0
    for line in data:
        extra = 4
        length += len(line)
        for char in line[1:-1]:
            if char == "\\" or char == '"':
                extra += 1
        encodeLenght += len(line) + extra
        # print(encodeLenght)
    total = encodeLenght - length
    return total, length, encodeLenght


def main():
    data = getData()
    totalP1, length, memory = partOne(data)
    print("Part one: CharacterCount is %s, memoryCode is %s, Total is %s - %s = %s" %(length, memory, length, memory, totalP1))
    totalP2, length, encodeLenght = partTwo(data)
    print("Part one: New CharacterCount is %s, old CharacterCount is %s, Total is %s - %s = %s" %(encodeLenght, length, encodeLenght, length, totalP2))
main()