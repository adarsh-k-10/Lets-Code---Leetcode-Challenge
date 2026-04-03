class Solution(object):
    def reverseWords(self, s):
        
        words = s.split()
        res = ""
        for i in words:
            w  = i[::-1]
            res += w + " "
        return res.strip()