class Solution(object):
    def numberGame(self, nums):
        
        nums.sort(reverse = True)
        result = []
        while nums:
            a = nums.pop()
            b = nums.pop()
            result.append(b)
            result.append(a)

        return result