import string

def getData():
    data = []
    # for line in open("2022/Day_03/TestData.txt"):
    for line in open("2022/Day_03/Data.txt"):
        line = line.rstrip()
        lineP1 = line[:len(line)//2]
        lineP2 = line[len(line)//2:]
        data.append([lineP1, lineP2])
    # print(data)
    return data

def getPriority(data):
    total = 0
    for line in data:
        for character in line[0]:
            # print(character)
            if character in line[1]:
                # print(character)
                if character.isupper():
                    total += string.ascii_uppercase.index(character) + 1 + 26
                else:
                    total += string.ascii_lowercase.index(character) + 1
                break
    # print(total)
    return total
            
def getCommonPriority(data):
    newData = []
    total = 0
    for line in data:           # rejoin compartments
        line = line[0] + line[1]
        # print(line)
        newData.append(line)
    # print(newData)
    for line in range(0, len(newData), 3):
        for letter in newData[line]:
            # print(letter)
            if letter in newData[line + 1] and letter in newData[line + 2]:
                if letter.isupper():
                    total += string.ascii_uppercase.index(letter) + 1 + 26
                else:
                    total += string.ascii_lowercase.index(letter) + 1
                break
                
    # print(total)
    return total


def main():
    data = getData()
    P1 = getPriority(data)
    print("Part one, item priority total is %s" %(P1))
    P2 = getCommonPriority(data)
    print("Part two, item priority for team stickers is %s" %(P2))
main()