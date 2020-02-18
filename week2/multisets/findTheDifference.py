
# incomplete, code doesn't pass
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set_s = set(s)
        set_t = set(t)
        if(set_s == set_t):
            elem = set_s.pop()
            return elem
        set_a = set_s.difference(set_t)
        set_b = set_t.difference(set_s)
        
        if(len(set_a) == 0):
            elem = set_b.pop()
            return elem
        else:
            elem = set_a.pop()
            return elem