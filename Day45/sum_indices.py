class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        
        total = 0
        for i in range(len(nums)):
            count = 0
            j= i
            while j > 0:
                if j%2 == 1:
                    count += 1
                j //= 2
            if count == k:
                total += nums[i]
        
        return total
