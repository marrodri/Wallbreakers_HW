
    
def popListNum(s: list, i:int):
    n = 0
    # print("pop list NUM:")
    # print(s)
    while(n < i):
        s.pop(0)
        n += 1

def starPattern(s: list, c: str):
    while s:
        if(s[0] == c):
            s.pop(0)
        else:
            break
            
def dotstarPattern(string:list, pattern:list):
    print("dotstart string")
    print(string)
    print("pattern")
    print(pattern)
    while(len(pattern) > 1):
        if(pattern[0] == '.' and pattern[1] == '*'):
            popListNum(pattern, 2)
        elif(pattern[0] == '.' and pattern[1] != '*'):
            pattern.pop(0)
        if(pattern[0] != '*' and pattern[0] != '.'):
            break
        
    if(pattern):
        while(string):
            string.pop(0)
            if(string[0] == pattern[0]):
                break;
    else:
        while(string):
            string.pop(0)
                
    
        
def regexBase(string: list, pattern: list):
    if(not string or not pattern):
        return False
    if(len(pattern) > 1):
        if(pattern[0].isalpha() and (pattern[1] == '*')):
            return True
    if((string[0] == pattern[0]) or (pattern[0] == '.')):
        return True
    return False
        
class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        if (p == ".*"):
            return True
        regex_lst = list(p)
        string_lst = list(s)
        if(regex_lst[0] == '*'):
            return False
        while(regexBase(string_lst, regex_lst)):
            # print("current patt:")
            # print(regex_lst)
            # print("current str:")
            # print(string_lst)
            checker = 0
            if(len(regex_lst) > 1):
                if(regex_lst[0] == '.' and regex_lst[1] == '*'):
                    dotstarPattern(string_lst, regex_lst)
                    checker = 1
            if(len(regex_lst) > 1 and checker == 0):
                if(regex_lst[0].isalpha() and regex_lst[1] == '*'):
                    starPattern(string_lst, regex_lst[0])
                    popListNum(regex_lst, 2)
                    checker = 1
            if(regex_lst and string_lst and checker == 0):
                if(regex_lst[0] == '.' or regex_lst[0] == string_lst[0]):
                    regex_lst.pop(0)
                    string_lst.pop(0)
                
        print("printing string hoping its empty:")
        print(string_lst)
        if(not string_lst and not regex_lst ):
            return True
        return False