
# final answer
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp = n
        if(tmp <= 0):
            return False
        while(tmp > 1):
            if(tmp % 2 != 0):
                print(tmp % 2)
                return False
            tmp = tmp / 2
        return True
        