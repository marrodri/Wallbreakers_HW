
# this one is still not working, incomplete

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        patt_dict = {}
        patt_lst = list(pattern)
        str_lst = str.split(' ')
        print(patt_lst)
        print(str_lst)
        if(len(pattern) != len(str)):
            return False
        for patt,wrd in zip(patt_lst, str_lst):
            if(patt not in patt_dict.keys() and wrd not in patt_dict.values()):
                patt_dict[patt] = wrd
            elif(patt in patt_dict.keys() and patt_dict[patt] == wrd):
                print("continue")
                print(patt_dict[patt])
                print(patt)
                pass
            else:
                return False
        return True
            