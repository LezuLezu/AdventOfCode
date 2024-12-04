import re

def getData():  
    # with open("2024/Day_03/testData.txt", "r") as file:
    # with open("2024/Day_03/testData2.txt", "r") as file:
    with open("2024/Day_03/Data.txt", "r") as file:
        data = file.read()
    return data

def findMulti(data):
    results = 0
    # regex key to find complete patterns
    finderKey = r"mul\((\d+),(\d+)\)"
    # reges patterns to fetch only the ints
    finderkeyInts = r"mul\((\d+),(\d+)\)"
    matches = re.findall(finderkeyInts, data)
    # print(matches)
    matchNums = [(int(a), int(b)) for a, b in matches]
    # print(matchNums)
    for line in matchNums:
        results += line[0] * line[1]
    return results

def dodont(data):
    do_ex = r"do\(\)"
    dont_ex = r"don't\(\)"
    # Regex to find `do()` and `don't()` commands
    pattern = r"(do\(\)|don't\(\))"
    matches = [(m.group(), m.start()) for m in re.finditer(pattern, data)]
    matches.append(("end", len(data)))
    captured_data = []
    collecting = True
    last_end = 0  
    for i in range(len(matches)):
        command, start = matches[i]        
        if collecting:
            captured_data.append(data[last_end:start].strip())        
        if command == "don't()":
            collecting = False
        elif command == "do()":
            collecting = True        
        last_end = start + len(command)

    # Combine collected fragments
    final_data = " ".join(captured_data).strip()
    # print("Collected data:", final_data)
    results = findMulti(final_data)
    # print(results)
    return results

def main():
    data = getData()
    # print(data)
    part1 = findMulti(data)
    print("Part one, multiplications of corrupted data: %s"%(part1))
    part2 = dodont(data)
    print("Part two, enabled functions multiplications of corrupted data: %s"%(part2))
    
if __name__ == "__main__":
    main()