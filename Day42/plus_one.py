class Solution(object):
    def plusOne(self, digits):

        if digits[-1] != 9:
            digits[-1] += 1
        
        else:
            for i in range(1,len(digits) + 1):
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] += 1
                    return digits
            digits = [1] + digits

        return digits
