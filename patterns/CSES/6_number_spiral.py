import sys


control = []
def make_spiral(size: int):
    spiral = [[0 for i in range(size)] for j in range(size)]
    # print(spiral)
    spiral[0][0] = 1
    # spiral[1][1] = 10
    # print(spiral)
    for i in range(1, size):
        # print(f"i: {i}")
        if i % 2 != 0:
            last_num = spiral[0][i - 1]
            # print(f"first last {last_num}")
            for j in range(i):
                last_num += 1
                spiral[j][i] = last_num
                # print(f"e1 [{j}][{i}]: {spiral[j][i]}")
                # print(spiral)
                
            # last_num = spiral[i][i]
            # print(f'second last_num {last_num}')
            for j in range(i, 0-1, -1):
                last_num += 1
                spiral[i][j] = last_num 
                # print(f"e2 [{i}][{j}]: {spiral[i][j]}")
                # print(spiral)
            # print(spiral, end="\n")
            # break

        else:
            last_num = spiral[i - 1][0]
            for j in range(i):
                last_num += 1
                spiral[i][j] = last_num
                # print(f"o1 [{j}][{i}]: {spiral[i][j]}")

            # last_num = spiral[i][i]
            for j in range(i, 0-1, -1):
                last_num += 1
                spiral[j][i] = last_num 
                # print(f"o2 [{j}][{i}]: {spiral[i][j]}")
            # print(spiral, end="\n")   
            # break
    print(spiral)   
    # return spiral



if __name__ == "__main__":

    # num = int(sys.argv[1].strip())
    # num_list = sys.argv[2:]
    # print(num_list)
    spiral = make_spiral(10)

    # lines = sys.stdin.readlines()[1:]
    # lines_clean = []
    # for l in lines:
    #     l = l.split(" ")
    #     lines_clean.append((int(l[0]), int(l[1])))
    # max_input = max(max(lines_clean))
    # spiral = make_spiral(max_input)
    # for cord in lines_clean:
    #     print(spiral[cord[0]][cord[1]])






class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        matches = {}
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                diff = -1 * (nums[i] + nums[j])
                if (diff in nums_set) and diff in nums[j+1:]:
                    array = tuple(sorted([nums[i], nums[j], diff], reverse=True))
                    matches[array] =  1
        
        return list(matches.keys())
