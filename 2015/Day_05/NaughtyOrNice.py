def getData():
    data = []
    for line in open('2015/Day_05/data.txt', 'r'):
        items = line.rstrip('\n')
        data.append(items)
    # print(data)
    return data


# Part one
vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']

def isNice_P1(string):
    vowelCount = 0
    badStringCount = 0
    doubleLetter = False
    for i in range(len(string)):
        if string[i] in vowels:
            vowelCount += 1
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                doubleLetter = True
            if string[i] + string[i + 1] in badStrings:
                badStringCount += 1
    if vowelCount >= 3 and doubleLetter and badStringCount == 0:
        return True
    else:
        return False

def isNice_P2(string):
    doublePair = False
    repeatLetter = False
    for i in range(len(string)):
        if i < len(string) - 3:
            if string[i] + string[i + 1] in string[i + 2:]:
                doublePair = True
        if i < len(string) - 2:
            if string[i] == string[i + 2]:
                repeatLetter = True
    if doublePair and repeatLetter:
        return True
    else:
        return False


def main():
    data = getData()
    # part 1
    niceCount_P1 = 0
    for string in data:
        if isNice_P1(string):
            niceCount_P1 += 1
    print("Number of nice strings: %s" %(niceCount_P1))
    # part 2
    niceCount_P2 = 0
    for string in data:
        if isNice_P2(string):
            niceCount_P2 += 1
    print("Number of nice strings: %s" %(niceCount_P2))

main()