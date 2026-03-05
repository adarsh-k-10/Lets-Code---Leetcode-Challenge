class Solution(object):
    def subtractProductAndSum(self, n):
        
        total_sum = 0
        product = 1
        for digit in str(n):
            total_sum += int(digit)
            product *= int(digit)

        return product - total_sum
