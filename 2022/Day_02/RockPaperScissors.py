# A -> Rock
# B -> Paper
# C -> Scissors

#  Part one
# X -> Rock         -> 1 point
# Y -> Paper        -> 2 points
# Z -> Scissors     -> 3 points

#  Part two
# X -> Lose        
# Y -> Draw
# Z -> Win

# Win -> 6 points + item score
# Tie -> 3 points + items score
# Loss -> 0 points + item score

itemsDict = {"A": "Rock", "B": "Rock", "C": "Scissors", 
            "X": ["Rock", 1], "Y": ["Paper", 2], "Z": ["Scissors", 3]}


def getData():
    data = []
    # for line in open("2022/Day_02/TestData.txt", "r"):
    for line in open("2022/Day_02/Data.txt", "r"):
        items = line.rstrip('\n').split(' ')
        data.append(items)        
    # print(data)
    return data

def findScore(data):
    score = 0
    for match in data:
        # Ties
        if match[0] == "A" and match[1] == "X" :
            score += 3
            score += 1
        if match[0] == "B" and match[1] == "Y" :
            score += 3
            score += 2
        if match[0] == "C" and match[1] == "Z" :
            score += 3
            score += 3
        # Wins
        if match[0] == "A" and match[1] == "Y":
            score += 6
            score += 2
        if match[0] == "B" and match[1] == "Z":
            score += 6
            score += 3
        if match[0] == "C" and match[1] == "X":
            score += 6
            score += 1
        # loses
        if match[0] == "A" and match[1] == "Z":
            score += 0
            score += 3
        if match[0] == "B" and match[1] == "X":
            score += 0
            score += 1
        if match[0] == "C" and match[1] == "Y":
            score += 0
            score += 2
    # print(score)
    return score

def findScore_p2(data):
    score = 0
    for match in data:
        # Losses
        if match[0] == "A" and match[1] == "X" :
            score += 0
            score += 3
        if match[0] == "B" and match[1] == "X" :
            score += 0
            score += 1
        if match[0] == "C" and match[1] == "X" :
            score += 0
            score += 2

        #  Wins
        if match[0] == "A" and match[1] == "Z" :
            score += 6
            score += 2
        if match[0] == "B" and match[1] == "Z" :
            score += 6
            score += 3
        if match[0] == "C" and match[1] == "Z" :
            score += 6
            score += 1

        # Ties
        if match[0] == "A" and match[1] == "Y" :
            score += 3
            score += 1
        if match[0] == "B" and match[1] == "Y" :
            score += 3
            score += 2
        if match[0] == "C" and match[1] == "Y" :
            score += 3
            score += 3
    return score

def main():
    data = getData()
    score_P1 = findScore(data)
    print("Part one: You have a Score of %s points" %(score_P1))

    score_P2 = findScore_p2(data)
    print("Part two: You have a Score of %s points" %(score_P2))
main()