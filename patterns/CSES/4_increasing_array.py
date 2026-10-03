import sys

control = []

def calculate_steps(array: str):

    total_steps = 0
    for i in range(1, len(array)):
        diff =  array[i] - array[i - 1]
        if diff < 0:
            total_steps += abs(diff)
            array[i] += abs(diff)
    print(total_steps)
        


if __name__ == "__main__":

    # array = sys.argv[1].strip().strip().split() 
    array = sys.stdin.readlines()[1].strip().split()
    array = [int(i) for i in array]
    calculate_steps(array)



