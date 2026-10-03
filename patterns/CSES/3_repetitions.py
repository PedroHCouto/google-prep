import sys

control = []

def longest_rep(array: str):

    max_sequ = 1
    control = 1
    prev_l = ""
    for l in array:

        if l == prev_l:
            control += 1
        else:
            max_sequ = max(max_sequ, control)
            control = 1
        prev_l = l

    max_sequ = max(max_sequ, control)
    print(max_sequ)


if __name__ == "__main__":

    # array = str(sys.argv[1])
    array = str(sys.stdin.readlines()[0]).strip()
    longest_rep(array)



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            

            for j in range(i + 1, len(numbers)):

                s = numbers[i] + numbers[j]
                if s == target:
                    return [i+1, j+1]

                elif (numbers[i] == numbers[j]) or (s > target):
                    break