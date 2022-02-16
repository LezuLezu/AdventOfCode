import numpy as np

def getData(path):
    data = []
    with open(path) as file:
        tempList = []
        for line in file:
            items = line.strip().split("\n")
            for item in items:
                # print(item)
                if item.startswith("---"):
                    # print(item)
                    if "0" in item:
                       continue
                    else:
                        data.append(tempList)
                        tempList = []
                else:
                    # print("in else")
                    if item != "":
                        # print("in temp append")
                        tempList.append([int(x) for x in item.split(",")])
                        # print("added")
        data.append(tempList)       # add last list
    # for line in data:
    #     print(line)
    # print(data)
    return data
                
def findProbes(data):
    probes = 0
    sets = iter(map(set, *data))
    result = sets.next()
    for s in sets:
        result = result.intersection(s)
    print(result)



if __name__ == '__main__':
    test_data = getData("Day_19/test_data.txt")
    # data = getData("Day_19/data.txt")

    findProbes(test_data)
