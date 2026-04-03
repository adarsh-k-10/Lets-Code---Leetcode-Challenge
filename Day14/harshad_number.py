class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        
        total = 0
        for i in str(x):
            total += int(i)
        
        return total if x%total == 0 else -1