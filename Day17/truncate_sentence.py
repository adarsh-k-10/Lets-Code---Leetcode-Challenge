class Solution(object):
    def truncateSentence(self, s, k):
        
        words = s.split()
        res = " ".join(words[:k])
        
        return res