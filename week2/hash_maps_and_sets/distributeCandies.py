
# exercise done

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        set_candie = set(candies)
        len_set = len(set_candie)
        
        if(len_set >= len(candies)/2):
            return int(len(candies)/2)
        else:
            return len_set
        
        