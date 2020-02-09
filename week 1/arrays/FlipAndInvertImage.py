
# final answer

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for array in A:
            i = 0
            array.reverse()
            print(array)
            for elem in array:
                if(elem == 0):
                    array[i] = 1
                else:
                    array[i] = 0
                i += 1
        return A