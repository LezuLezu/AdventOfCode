startPostion = 50

def getData():
    data = []
    # with open('2025/Day_01/testData.txt', 'r') as file:
    with open('2025/Day_01/data.txt', 'r') as file:
        data = file.read().splitlines()
    return data

def sequence(position, data):
    code = 0
    for line in data:
        direction, steps = rotation(line)
        if direction == "L":
            position = (position - steps) % 100
        else:  # direction == "R"
            position = (position + steps) % 100

        if position == 0:
            code += 1
    return code

def sequencePart2(position, data):
    code = 0
    for line in data:
        direction, steps = rotation(line)

        step = -1 if direction == "L" else 1
        for i in range(steps):
            position = (position + step) % 100

            if position == 0:
                code += 1
    return code


def rotation(turn):
    direction = turn[0]
    steps = int(turn[1::])
    # print(direction, steps)
    return direction, steps


def main():

    data = getData()
    # print(data)
    code = sequence(startPostion, data)
    print("Passcode part 1 = %s" %(code))

    code2 = sequencePart2(startPostion, data)
    print("Passcode part 1 = %s" %(code2))


main()
