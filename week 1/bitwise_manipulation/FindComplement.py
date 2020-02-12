

# INCOMPLETE

class Solution:
    def findComplement(self, num: int) -> int:
        if(num == 2):
            return 1
        if(num <= 1):
            return 0
        num_com = 0
        bit_extr =  0
        while(num):
            bit_extr = num & 1
            if(bit_extr ^ 1):
                num_com = num_com | 1
            num = num >> 1
            if(num):
                num_com = num_com << 1    
        return num_com
