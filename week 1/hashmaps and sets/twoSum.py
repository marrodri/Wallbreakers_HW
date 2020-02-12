
# incomplete, ask how to

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        arr_size = len(nums)
        while (i < arr_size):
            j = 0
            while(j < arr_size):
                if ((nums[i] + nums[j] == target) and i != j):
                    return set([i,j])
                j += 1
            i += 1

        # dictionary
        # for every number have their key
        # their value will be store exactly to the index of the array