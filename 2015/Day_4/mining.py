from hashlib import md5
import hashlib
from itertools import count

def solve_5(puzzle):
    for x in count(1):
        hash = puzzle + str(x)
        test =  md5(hash.encode('utf-8')).hexdigest()
        if test[:5] == "00000":
            print(x)
            break

def solve_6(puzzle):
    for x in count(1):
        hash = puzzle + str(x)
        test =  md5(hash.encode('utf-8')).hexdigest()
        if test[:6] == "000000":
            print(x)
            break


def main():
    puzzle = "ckczppom"
    solve_5(puzzle)
    solve_6(puzzle)

main()