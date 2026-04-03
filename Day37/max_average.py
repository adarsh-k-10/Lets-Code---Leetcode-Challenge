class Solution(object):
    def findMaxAverage(self, nums, k):

        max_sum = sum(nums[:k])
        curr_sum = max_sum

        for i in range(k,len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            if max_sum < curr_sum:
                max_sum = curr_sum

        return float(max_sum) / k