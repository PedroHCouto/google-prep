import sys
from math import ceil

control = []

def get_permutations(num: int):
    if num == 1:
        print(1)
        return
    if num < 4:
        print("NO SOLUTION")
        return

    output = ""
    for i in range(2, num + 1, 2):
        output += str(i) + " " 
    for i in range(1, num + 1, 2):
        output += str(i) + " " 
    
    print(output)

if __name__ == "__main__":

    # num = int(sys.argv[1].strip())
    num = int(sys.stdin.readlines()[0].strip())
    get_permutations(num)



