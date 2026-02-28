class Solution(object):
    def findGCD(self, nums):
        
        small = min(nums)
        large = max(nums)
        
        while small != 0:
            large, small = small, large % small
        return large