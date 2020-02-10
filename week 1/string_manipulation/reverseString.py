
# final answer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = 0
        while i < len(s)/2:
            j = (i + 1) * -1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            