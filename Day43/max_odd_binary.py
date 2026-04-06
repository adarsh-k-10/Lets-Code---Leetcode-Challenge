class Solution(object):
    def maximumOddBinaryNumber(self, s):
        
        b = list(s)
        b.sort(reverse = True)
        for i in range(len(b)):
            if b[i] == '0':
                break

        b[-1],b[i-1] = b[i-1],b[-1]
        res = ''.join(b)

        return res
