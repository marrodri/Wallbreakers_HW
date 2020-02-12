
# Incomplete

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            j = (i + 1) * -1
            if(not s[i].isalpha):
                i += 1

# union find
# it can be seen as a tree, each node has a parent, 
# parent, 

# same region, common parents

# dfs, it may take longer time, with the longer

# it doesn't matter there's only parent]
# override parent

# sets the parent of 2 different elements
# diferent parents, to unite those 2 graphs, set a parent of anther parent
# to become part of the same region

# if they're the same elements, they're connected, if they're not, they will be
# connected

