
# incomplete

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        arr_lst = list(s);
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while(i < j):
            if(s[i] in vowel and s[j] in vowel):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
            if(s[i] not in vowel):
                i += 1
            if(s[j] not in vowel):
                j -= 1
        return s
        