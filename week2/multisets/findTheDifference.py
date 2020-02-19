
# exercise done
import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        for char in t:
            if(s_count[char] < t_count[char]):
                return char
        return char