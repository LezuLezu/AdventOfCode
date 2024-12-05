import re

def getData():
    data = []
    # with open("2024/Day_05/testData.txt", 'r') as f:
    with open("2024/Day_05/data.txt", 'r') as f:
        data = f.readlines()
    return data    


def parseData():
    data = getData()
    rules = []
    updates = []
    for line in data:
        line = line.strip()
        if line == "":
            continue
        elif "|" in line:
            rules.append(tuple(line.split("|")))
        elif "," in line:
            updates.append(tuple(line.split(",")))
    return [rules, updates]


def checkRules(combinations, rules):
    for i in combinations:
        if i[::-1] in rules:
            return False
    return True


def FindMiddleSum(data):
    correctSum = 0
    rules = data[0]
    updates = data[1]
    fixedUpdateSum = 0
    for update in updates:
        combinations = []
        for index1, i in enumerate(update):
            for index2, j in enumerate(update):
                if index1 != index2:
                    combinations.append((i, j) if index1 < index2 else (j, i))
        result = checkRules(combinations, rules)
        if result:
            correctSum += int(update[int(len(update) / 2)])
        else:
            ordered_update = fixIncorrect(update, rules)
            fixedUpdateSum += int(ordered_update[int(len(ordered_update) / 2)])
        # print(sum, result, update)
    return correctSum, fixedUpdateSum

def fixIncorrect(update, rules):
    ordered_update = [update[0]]
    # print(ordered_update)
    for i in update[1:]:
        added = False
        j = 0
        while not added:
            if j == len(ordered_update):
                ordered_update.append(i)
                added = True
            elif (ordered_update[j], i) in rules or (
                i,
                ordered_update[j],
            ) not in rules:
                j = j + 1
            else:
                ordered_update.insert(j, i)
                added = True
    # print(ordered_update)
    return ordered_update




def main():
    data = parseData()
    # print(data)
    part1, part2 = FindMiddleSum(data)
    print("Part 1 middle sum : %s" %(part1))
    # print(incorrectUpdates)
    print("Part 2, middle sum of fixed updates: %s"%(part2))
   
if __name__ == "__main__":
    main()