
def getData():
    data = []
    with open('2015/Day_03/data.txt', 'r') as file:
        dataF = file.read()
        print(dataF)
        for i in range(len(dataF)):
            data.append(dataF[i])
        # print(data)
    return data

def getHouses(data):
    coords = [0,0]
    coord_list = ["0,0"]
    for x in data:
        if x == ">":
            coords[0]+=1
        if x == "<": 
            coords[0]-=1
        if x == "^":
            coords[1]+=1
        if x == "v":
            coords[1]-=1
        coord_list.append(str(coords[0])+","+str(coords[1]))
    return len(set(coord_list))

def getRoboHouses(data):
    s_coords = [0,0]
    r_coords = [0,0]
    coord_list = ["0,0"]
    i = 0
    for x in data:
        i+=1 
        if x == ">":
            if i % 2 == 0:
                s_coords[0]+=1
            else:
                r_coords[0]+=1
        if x == "<": 
            if i % 2 == 0:
                s_coords[0]-=1
            else:
                r_coords[0]-=1
        if x == "^":
            if i % 2 == 0:
                s_coords[1]+=1
            else:
                r_coords[1]+=1
        if x == "v":
            if i % 2 == 0:
                s_coords[1]-=1
            else:
                r_coords[1]-=1
        if i % 2 == 0:        
            coord_list.append(str(s_coords[0])+","+str(s_coords[1]))
        else:
            coord_list.append(str(r_coords[0])+","+str(r_coords[1]))
        
    return len(set(coord_list)) 

def main():
    data = getData()
    print(data)
    print("Part One, more than once visited: %s" %(getHouses(data)))
    print("Part two: %s" %(getRoboHouses(data)))
main()