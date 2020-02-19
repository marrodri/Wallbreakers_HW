
# exercise done

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = collections.Counter(s)
        i = 0
        for char in s:
            if(count_dict[char] == 1):
                return i
            i += 1
        return -1
# counter data type
# 