import sys

control = []

def missing_num(nums: list, max_num: int):
    nums_set = set(nums)
    for i in range(1, max_num+1):
        if str(i) not in nums_set:
            print(i)
            break


if __name__ == "__main__":

    # data = str(sys.argv[1]).split(" ")
    input_lines = sys.stdin.readlines()
    max_int = int(input_lines[0])
    data = str(input_lines[1].strip()).split(" ")

    # print(data)

    missing_num(data, max_num=max_int)

