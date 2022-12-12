import numpy as np

def getData():
    with open("2022/Day_11/TestData.txt") as file:
    # with open("2022/Day_11/Data.txt") as file:
        fileRead = file.read()
    dataFile = fileRead.split('\n\n')
    # print(fileRead)
    data = []
    for m in dataFile:
        monkeyInfo=m.split("\n")
        monkey ={
                    "items":[int(x) for x in monkeyInfo[1].split(": ")[1].split(", ")],
                    "operation": "".join(monkeyInfo[2].split(": ")[1].split(" ")[2:]),
                    "test": int(monkeyInfo[3].split(": ")[1].split(" ")[2]),
                    "toMonkey": [int(monkeyInfo[5].split(": ")[1].split(" ")[3]),int(monkeyInfo[4].split(": ")[1].split(" ")[3])],
                    "inspectCounter": 0
                }
        data.append(monkey)
    return data

def getMonkeyBusiness(data, amountOfRounds, devide):
    maxWorry = int(np.prod([monkey['test'] for monkey in data]))
    print(maxWorry)

    for rounds in range(amountOfRounds):
        for monkey in data:
            for item in monkey["items"]:
                item = eval(monkey["operation"].replace("old", "item"))
                if devide:
                    item = item // 3
                else:
                    item = item % maxWorry
                data[monkey["toMonkey"][item % monkey["test"] == 0]]["items"].append(item)   
                monkey["inspectCounter"] +=1
            monkey["items"] = []

    # print(data)
    inspectList = []
    for monkey in data:
        inspectList.append(monkey["inspectCounter"])
    inspectList.sort()
    print(inspectList)
    return inspectList[-1] * inspectList[-2]

def main():
    data = getData()
    # print(data)
    p1 = getMonkeyBusiness(data, 20, True)
    print("Hightes monkey businesses : %s" %(p1))
    p2 = getMonkeyBusiness(data, 10000, False)
    print("Hightes monkey businesses : %s" %(p2))

main()