
import collections

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        collect = collections.Counter(nums)
        lst = list()
        print(collect)
        i = 0
        lack_num = 0
        dup_num = 0
        while i < len(nums) and (lack_num is 0 or dup_num is 0):
            if(collect[i + 1] == 0 and lack_num is 0):
                lack_num = i + 1
                print(lack_num)
            if(collect[i + 1] == 2 and dup_num is 0):
                dup_num = i + 1
                print(dup_num)
            i += 1
        lst.append(dup_num)
        lst.append(lack_num)
        return lst
