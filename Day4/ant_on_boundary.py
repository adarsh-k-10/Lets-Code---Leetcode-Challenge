class Solution(object):
    def returnToBoundaryCount(self, nums):
        
        count = 0
        d = 0
        for num in nums:
            d += num
            if d == 0:
                count += 1
        
        return count
