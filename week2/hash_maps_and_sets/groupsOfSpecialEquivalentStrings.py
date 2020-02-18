
# still incomplete, the code doesn't pass the

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        order_dict = {}
        check = 0
        
        for word in A:
            lst_wrd = list(word)
            print(lst_wrd)
            i = 0
            check = 0
            print("rotating word!")
            while(i < len(lst_wrd)):
                tmp_str = ""
                tmp_str = tmp_str.join(lst_wrd)
                print(tmp_str)
                if(tmp_str in order_dict.keys()):
                    print("exist group incrementing")
                    order_dict[tmp_str] += 1
                    check = 1
                    break
                else:
                    lst_wrd = lst_wrd[1:] + lst_wrd[:1]
                    print(lst_wrd)
                    i += 1
            if(check is 0):
                print("adding new group")
                
                tmp_str = ""
                tmp_str = tmp_str.join(lst_wrd)
                print(tmp_str)
                order_dict[tmp_str] = 0
            print(order_dict)
        return len(order_dict)

# got tip from victoria with the use of an even list and an odd list