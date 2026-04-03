class Solution(object):
    def isPerfectSquare(self, num):
        
        num_root = int(sqrt(num))
        
        return num_root*num_root == num