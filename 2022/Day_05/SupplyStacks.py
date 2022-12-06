
# testStacks = {
#     "1" : ["Z", "N"],
#     "2" : ["M", "C", "D"],
#     "3" : ["P"]
# }

# stacks = {
#     "1" : ["V", "C", "D", "R", "Z", "G", "B", "W"],
#     "2" : ["G", "W", "F", "C", "B", "S", "T", "V"],
#     "3" : ["C", "B", "S", "N", "W"],
#     "4" : ["Q", "G", "M", "N", "J", "V", "C", "P"],
#     "5" : ["T", "S", "L", "F", "D", "H", "B"],
#     "6" : ["J", "V", "T", "W", "M", "N"],
#     "7" : ["P", "F", "L", "C", "S", "T", "G"],
#     "8" : ["B", "D", "Z"],
#     "9" : ["M", "N", "Z", "W"],
# }

crates = """
[W] [V]     [P]                    
[B] [T]     [C] [B]     [G]        
[G] [S]     [V] [H] [N] [T]        
[Z] [B] [W] [J] [D] [M] [S]        
[R] [C] [N] [N] [F] [W] [C]     [W]
[D] [F] [S] [M] [L] [T] [L] [Z] [Z]
[C] [W] [B] [G] [S] [V] [F] [D] [N]
[V] [G] [C] [Q] [T] [J] [P] [B] [M]
 1   2   3   4   5   6   7   8   9 
"""

crates = crates.splitlines()[1:-1] 

stacks = []
for s in range(9):
    stacks.append([])

for line in crates:
    for i, char in enumerate(line[1::4][::-1]): #Elk 4e caracter is de letter of een spatie als ie leeg is
        stacks[i].append(char)

print(stacks)

stacks = {
            "1" : [],
            "2" : [], 
            "3" : [],
            "4" : [],
            "5" : [],
            "6" : [],
            "7" : [],
            "8" : [],
            "9" : [],
        }
for line, i in crates[-1], stacks.keys():
    # print(line)
    for crate in line:
        stacks[str(i + 1)] = stacks[str( i + 1)].append(crate)
print(stacks)

def getMoves():
    moves = []
    for line in open("2022/Day_05/TestData.txt"):
    # for line in open("2022/Day_05/Data.txt"):
        if line.startswith("move"):
            line = line.split()
            # print(line)
            newLine = [line[1], line[3], line[-1]]
            # print(newLine)
            moves.append(newLine)
    # print(moves)
    return moves

def getTopCrates(moves):
    # for line in moves:
    #     # print(line)
    #     for crates in range(int(line[0])):
    #         # print(crates)
    #         testStacks[line[2]].append(testStacks[line[1]].pop())
    #     # print(testStacks)
    # topItems = [testStacks[key][-1] for key in testStacks]
    for line in moves:
        for crates in range(int(line[0])):
            stacks[line[2]].append(stacks[line[1]].pop())
    topItems = [stacks[key][-1] for key in stacks]
    # print(topItems)
    # print(testStacks)
    return topItems
        
def main():
    moves = getMoves()
    # p1 = getTopCrates(moves)
    # print("Part one, top Stacks %s"%''.join(p1))
main()

