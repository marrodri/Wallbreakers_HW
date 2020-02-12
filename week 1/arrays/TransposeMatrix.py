

# still not working
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        list_len = len(A)
        elem_len = len(A[0])
        final_list = [[None] * list_len] * elem_len
        i = 0
        j = 0
        for arr in A:
            i = 0
            for val in arr:
                final_list[i][j] = val
                i += 1
            j += 1
        return final_list