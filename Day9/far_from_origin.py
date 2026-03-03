class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        
        pos = 0
        blank = 0

        for move in moves:
            if move == "L":
                pos -= 1
            elif move == "R":
                pos += 1
            elif move == "_":
                blank += 1

        return abs(pos) + blank
