
# Exercise done

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_dict = {}
        for stone in S:
            for jewel in J:
                if(stone == jewel):
                    if(jewel in j_dict.keys()):
                            j_dict[jewel] += 1
                    else:
                        j_dict[jewel] = 1
        return (sum(j_dict.values()))
        