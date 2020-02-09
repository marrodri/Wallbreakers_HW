

# TO DO, incomplete
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        final_list = []
        tmp_list = []
        list_len = len(A)
        elem_len = len(A[1])
        i = 0
        while i < elem_len:
            for list in A[i]: