
# exercise done, it's super slow too

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_lst = []
        if(len(nums1) > len(nums2)):
            short_arr = nums2
            long_arr = nums1
        else:
            short_arr = nums1
            long_arr = nums2
        for check in short_arr:
            for num in long_arr:
                if(check == num and check not in inter_lst):
                    inter_lst.append(num)
                    long_arr = [new_num for new_num in long_arr if new_num != num]
                    print(long_arr)
        return inter_lst
           
        
        