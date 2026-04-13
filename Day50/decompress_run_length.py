class Solution(object):
    def decompressRLElist(self, nums):
        
        res = []
        for i in range(0,len(nums)-1,2):
            res.extend(nums[i]*[nums[i+1]])
        
        return res
