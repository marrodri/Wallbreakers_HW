

# Exercise done, it passes

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        wrd_dict = {}
        list_a = A.split( )
        list_b = B.split( )
        final_list = list()
        for word_a in list_a:
            if(word_a in wrd_dict.keys()):
                wrd_dict[word_a] += 1
            else:
                wrd_dict[word_a] = 1
        for word_b in list_b:
            if(word_b in wrd_dict.keys()):
                wrd_dict[word_b] += 1
            else:
                wrd_dict[word_b] = 1
        for key in wrd_dict.keys():
            if(wrd_dict[key] == 1):
                final_list.append(key)
        return final_list
            