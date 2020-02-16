
# Exercise Done, 
# note: learn a faster algorithm for this exercise

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        final_list = list()
        mc_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            tmp_list = list()
            print(len(word))
            for char in word:
                i = ord(char) - 97
                tmp_list.append(mc_list[i])
            print(tmp_list)
            if(''.join(tmp_list) in final_list):
                pass
            else:
                final_list.append(''.join(tmp_list))
        return len(final_list)