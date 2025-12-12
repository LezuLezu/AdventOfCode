from copy import deepcopy

def getData():
    with open("2024/Day_07/Data.txt", "r" ) as f:
        input = f.readlines()
    inputs =[[int(a), b.strip().split(' ')] for a, b in [e.split(":") for e in input]]
    return inputs
    
def findOperatorCombo(n, arr, results, i, part2 = False):
    if i == n:
        results.append(deepcopy(arr))
        return
    arr[i] = "+"
    findOperatorCombo(n, arr, results, i + 1, part2)
    arr[i] = "*"
    findOperatorCombo(n, arr, results, i + 1, part2)
    if not part2:
        return
    
    arr[i] = "||"
    findOperatorCombo(n, arr, results, i + 1, part2)


def makeCalculation(eq, operations, part2 = False):
    result = eq[0]
    operationsIndex = 0
    while True:
        numbers = [int(i) for i in eq[1]]
        total = numbers.pop(0)
        for i in range(len(operations[operationsIndex])):
            if operations[operationsIndex][i] == '+':
                total += numbers.pop(0)
            elif operations[operationsIndex][i] == '*':
                total *= numbers.pop(0)
                # p2
            elif operations[operationsIndex][i] == "||" and part2:
                nextNumber = numbers.pop(0)
                newNumber = str(total) + str(nextNumber)
                total = int(newNumber)
        if total == result:
            return True
        operationsIndex += 1
        if operationsIndex == len(operations):
            return False
        
def findSolutions(equations, part2 = False):
    accepted = []
    notAccepted = []
    countEquations = len(equations)
    for index, eq in enumerate(equations):
        operations = []
        gaps = len(eq[1]) - 1
        combinations = [None] * gaps
        findOperatorCombo(gaps, combinations, operations, 0, part2)
        print(f"\rEquation {index+1} of {countEquations}", end="")
        if makeCalculation(eq, operations, part2):
            accepted.append(eq[0])
        else:
            notAccepted.append(eq)
    return (accepted, notAccepted)


def main():
    print("Welcome to the Bridge Repair program!")
    data = getData()
    accepted, notAccepted = findSolutions(data)
    print("part 1: %s"%(sum(accepted)))
    (acceptedP2 , rejected) = findSolutions(notAccepted, True)
    print("part 2: %s"%(sum(acceptedP2)+ sum(accepted)))
      


if __name__ == "__main__":
    main()