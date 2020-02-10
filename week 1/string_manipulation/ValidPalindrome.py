
# Incomplete

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            j = (i + 1) * -1
            if(not s[i].isalpha):
                i += 1