def getData():
    data = []
    for line in open('2015/Day_02/data.txt', 'r'):
        items = line.rstrip('\n').split('x')
        items = [int(item.strip()) for item in items]
        data.append(items)
    # print(data)
    return data

#  2*L*W + 2*W*H + 2*H*L
# 2*3*4 -> L = 2, W = 3, H = 4 
#  2*2*3 + 2*3*4 + 2*4*2 
#  2*6 + 2 * 12 + 2*8 = 52
#smallest side for slack

def getSquareFeet(data):
    squareFeet = 0
    for present in range(len(data)):
        lenght = data[present][0]
        widht = data[present][1]
        height = data[present][2]
        lengtArea = height*lenght
        heightArea = widht * height
        widthArea = lenght*widht
        slack = min([widthArea, heightArea, lengtArea])
        # print(slack)
        sqFt = (2 * lengtArea) + (2 * heightArea) + (2 * widthArea) + slack
        squareFeet += sqFt
    return squareFeet

def getRibbonFeet(data):
    ribbonFeet = 0
    for present in range(len(data)):
        lenght = data[present][0]
        widht = data[present][1]
        height = data[present][2]
        presentSize = [lenght, height, widht]
        presentSize.sort()
        # print(presentSize)
        size_1 = presentSize[0]
        size_2 = presentSize[1]
        size_3 = presentSize[2]
        ribonWrap = size_1 + size_1 + size_2 + size_2
        ribbonFeet += ribonWrap 
        ribonBow = size_1 * size_2 * size_3
        ribbonFeet += ribonBow
    return ribbonFeet
        

def main():
    data = getData()
    print("Total Square Feet of wrapping paper: %s" %(getSquareFeet(data)))
    print("Total length of Ribbon needed: %s" %(getRibbonFeet(data)))
main()