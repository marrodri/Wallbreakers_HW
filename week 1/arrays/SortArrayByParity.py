

# fuction annotations "->"
# it can be used to attach additional information to the arguments or a return values of functions,
# another way to say how a function must be used.

# attach metadata to functions describing parameters and return values
# metadata: metadata is a library that provides for access to installed package metadata

List = [int]

# MY ANSWER
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        for num in A:
            if(num % 2 == 0):
                even_list.append(num)
            else:
                odd_list.append(num)
        return (even_list + odd_list)


# ans = Solution()
# ans.sortArrayByParity([3,1,2,4])
# print(sortArrayByParity())