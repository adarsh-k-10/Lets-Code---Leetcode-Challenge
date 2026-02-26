class Solution(object):
    def maxDepth(self, s):
        
        res = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                stack.pop()
            
            res = max(res,len(stack))

        return res