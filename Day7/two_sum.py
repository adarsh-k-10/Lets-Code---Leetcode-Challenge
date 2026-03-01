class Solution(object):
    def twoSum(self, nums, target):
      
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i]+nums[j] == target:
                    result.append(j)
                    result.append(i)
                    return result
                  
        return result
