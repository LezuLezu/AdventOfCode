
def getData():
    data = []
    dataB = []
    # with open("2022/Day_01/TestData.txt", 'r') as f:
    with open("2022/Day_01/Data.txt", 'r') as f:
        dataF = f.read()
        dataF = dataF.split('\n\n')
        dataF = [text.replace("\n", " ") for text in dataF]
        # print(dataF)
    for string in dataF:
        dataB.append(string.split(" "))
    data =[[int(x) for x in lst] for lst in dataB]    
    # print(data)
    return data

def findCarryingMostCalories(data):
    amountList = []
    for elf in data:
        amount = sum(elf)
        amountList.append(amount)
    maxAmount = max(amountList)
    carying = amountList.index(maxAmount)+1
    return carying, maxAmount

def findTopThreeMostCalories(data):
    amountList = []
    for elf in data:
        amount = sum(elf)
        amountList.append(amount)
    # print(amountList)
    amountListOrdered = amountList
    amountListOrdered.sort(reverse=True)
    # print(amountListOrdered)
    top3 = amountListOrdered[:3]
    # print(top3)
    totalAmountTop3 = sum(top3)
    elves = []
    for amount in top3:
       elf = amountList.index(amount) + 1
       elves.append(elf)
    return totalAmountTop3, elves    


def main():
    data = getData()
    mostCaryinElf, amount = findCarryingMostCalories(data)
    print("Part one: elf number %s is carrying %s calories" %(mostCaryinElf, amount))
    amount, elves = findTopThreeMostCalories(data)
    print("Part two: elves %s, %s and %s are carrying a total of %s calories" %(elves[0], elves[1], elves[2], amount))
main()