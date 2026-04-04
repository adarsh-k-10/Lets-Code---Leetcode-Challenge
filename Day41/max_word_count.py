  class Solution(object):
    def mostWordsFound(self, sentences):
        
        count = 0
        max_count = count
        for sentence in sentences:
            words = sentence.split()
            count = len(words)
            max_count = max(max_count, count)
        
        return max_count
