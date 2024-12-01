import numpy as np
from ast import literal_eval


def getData():
    with open ("2015/Day_06/data.txt", "r") as file:
        data= [line.split() for line in file]
    return data

def partOne(data):
    lights = np.zeros(shape=(1000, 1000), dtype=np.int64 )
    for instruction in data:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])

        if instruction[0] == "toggle":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x, y] = abs(lights[x, y] - 1)
        elif instruction[1] == "on":
            lights[x1:x2+1:1,y1:y2+1:1] = 1
        elif instruction[1] == 'off':
            lights[x1:x2+1:1,y1:y2+1:1] = 0

    lightCount = np.count_nonzero(lights)
    print("Part one : %s lights on" %(lightCount))

def partTwo(data):
    lights = np.zeros(shape=(1000, 1000), dtype=np.int64 )
    for instruction in data:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])

        if instruction[0] == "toggle":
            lights[x1:x2+1:1,y1:y2+1:1] += 2

        elif instruction[1] == "on":
            lights[x1:x2+1:1,y1:y2+1:1] += 1
        elif instruction[1] == 'off':
            lights[x1:x2+1:1,y1:y2+1:1] -= 1
            lights[lights < 0] = 0  # stop at 0

    brightness	= lights.sum()
    print("Part two : %s light brightness" %(brightness))  

def main():
    data = getData()
    # print(data)
    partOne(data)
    partTwo(data)
main()