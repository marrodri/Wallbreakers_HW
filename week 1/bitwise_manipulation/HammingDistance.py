
#Exercise done
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        i = 0
        while(x or y):
            x_extr = x & 1
            y_extr = y & 1
            if(x_extr ^ y_extr):
                i += 1
            x = x >> 1
            y = y >> 1
        return i