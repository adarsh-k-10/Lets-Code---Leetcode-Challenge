class Solution(object):
    def capitalizeTitle(self, title):
        
        words = title.split()
        res = []
        for word in words:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word.title())

        return " ".join(res)