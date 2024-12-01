def getData():
    data = []
    with open('2015/Day_01/data.txt', 'r') as file:
        dataF = file.read()
        # print(dataF)
        for i in range(len(dataF)):
            data.append(dataF[i])
    return data

def getFloor(data):
    floorCounter = 0
    for floor in range(len(data)):
        if data[floor] == "(":
            floorCounter += 1
        elif data[floor] == ")":
            floorCounter -= 1
    return floorCounter

def getBasement(data):
    floorCounter = 0
    for floor in range(len(data)):
        if data[floor] == "(":
            floorCounter += 1
        elif data[floor] == ")":
            floorCounter -= 1
        if floorCounter <= -1:
            return(floor + 1)
            
def main():
    data = getData()
    # print(data)
    print("Floor: %s " %(getFloor(data)))
    print("Basement position: %s " %(getBasement(data)))
    


main()