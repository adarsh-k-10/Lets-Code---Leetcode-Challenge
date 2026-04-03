import math

class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        n = len(dimensions)
        max_diagonal = 0
        max_area = 0

        for i in range(n):
            diagonal = math.sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)
            area = dimensions[i][0] * dimensions[i][1]

            if diagonal > max_diagonal or (diagonal == max_diagonal and area > max_area):
                max_diagonal = diagonal
                max_area = area

        return max_area