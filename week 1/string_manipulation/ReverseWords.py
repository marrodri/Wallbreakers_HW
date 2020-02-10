

# final answer

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split( )
        new_arr = ""
        for word in arr:
            new_arr = " ".join([new_arr, word[::-1]])
        new_arr = new_arr.strip()
        return new_arr
        