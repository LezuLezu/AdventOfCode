def get_data():
    data = []

    # with open('2025/Day_02/testData.txt', 'r') as file:
    with open('2025/Day_02/data.txt', 'r') as file:
        raw = file.read().replace("\n", "")   

    parts = raw.split(",")                  
    for p in parts:
        if not p.strip():                     
            continue
        a, b = p.split("-")                   
        data.append([int(a), int(b)]) 

    return data

def is_invalid_id(n: int):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def is_invalid_id_part2(n: int):
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue

        pattern = s[:k]
        repeats = L // k

        if repeats >= 2 and pattern * repeats == s:
            return True

    return False

def find_invalid_ids(ranges):
    invalids = []

    for low, high in ranges:
        ids = []
        for n in range(low, high + 1):
            if is_invalid_id(n):
                ids.append(n)
        invalids.append([low, high, ids])

    return invalids

def find_invalid_ids_part2(ranges):
    invalids = []

    for low, high in ranges:
        ids = []
        for n in range(low, high + 1):
            if is_invalid_id_part2(n):
                ids.append(n)
        invalids.append([low, high, ids])

    return invalids

def count_invalid_ID(invalids):
    count = 0
    for low, high, id in invalids:
        count += sum(id)
    return count

def main():
    data = get_data()
    # print(data)

    invalids = find_invalid_ids(data)
    p1_count = count_invalid_ID(invalids)
    print("Part one invalid count: %s" %(p1_count))

    p2_invalids = find_invalid_ids_part2(data)
    p2_count = count_invalid_ID(p2_invalids)
    print("Part 2 invalid id count: %s" %(p2_count))

main()