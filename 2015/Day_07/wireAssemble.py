def getData():
    with open("2015/Day_7/data.txt", "r") as file:
        data = [line.strip() for line in file]
    return data

def partOne(instructions):
    for i, line in enumerate(instructions):
        expression, var = line.split(' -> ')
        instructions[i] = '{} = {}'.format(var, expression)    
    
    for i,_ in enumerate(instructions):
        for key, val in operatorDict.items():
            instructions[i] = instructions[i].replace(key, val)

    completed = set()
    wires = {}

    while len(completed) != len(instructions):
        for line in instructions:
            try:
                exec(line, {}, wires)
                completed.add(line)
            except NameError:
                pass

    return 'wire a = {}'.format(wires['a'])

    

operatorDict = {'NOT':'~', 'AND':'&', 'OR':'|', 'LSHIFT':'<<', 'RSHIFT':'>>',
            'as':'_as', 'if':'_if', 'or':'_or', 'in':'_in', 'is':'_is'}
    
def main():
    data = getData()
    # print(data)
    print("Part One: %s" %(partOne(data)))
main()