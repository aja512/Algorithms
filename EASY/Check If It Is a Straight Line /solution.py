class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if all(x == coordinates[0][0] for x, y in coordinates):
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        if x2 - x1 == 0:
            return False
            
        m = (y2 - y1) / (x2 - x1)
        b = y1 - (m * x1)

        for i in coordinates:
            if i[0] * m + b != i[1]:
                return False

        return True
