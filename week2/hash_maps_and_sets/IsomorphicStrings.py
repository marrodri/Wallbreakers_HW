
# final answer, it still slow

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        if (len(s) != len(t)):
            return False
        for(chr_s, chr_t) in zip(s, t):
            if(chr_s in map_dict.keys() and map_dict[chr_s] is chr_t):
                print(chr_s)
                print(chr_t)
                pass
            elif(chr_s not in map_dict.keys() and chr_t not in map_dict.values()):
                print(chr_s)
                print(chr_t)
                map_dict[chr_s] = chr_t
            else:
                return False
        return True