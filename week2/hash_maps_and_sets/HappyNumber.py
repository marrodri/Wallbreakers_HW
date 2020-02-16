

# wrong answer, the algorithm is too slow
# also learn numpy.power


import numpy

class Solution:
    def isHappy(self, n: int) -> bool:
        
        numbers = list()
        total = 0
        while (1):
            tmp = n % 10
            n /= 10
            tmp = int(tmp)
            numbers.append(tmp)
            n = int(n)
            if(n == 0):
                power_list = numpy.power(numbers, 2)
                total = sum(power_list)
                n = total
                numbers.clear()
            if(total == 1):
                break
        return True
        