

# FInAL ANSWER
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        array = []
        i = left
        for num in range(left, right + 1):
            res = [int(x) for x in str(num)]
            j = 0
            if(not(0 in res)):
                for elem in res:
                    if(num % elem is not 0):
                        break
                    j += 1
                if(j is len(res)):
                    array.append(num)
            i += 1
        return array