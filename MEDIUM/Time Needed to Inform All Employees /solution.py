class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:        
        def calculateTime(n: int) -> int:
            if manager[n] != -1:
                informTime[n] += calculateTime(manager[n])
                manager[n] = -1
            return informTime[n]
        
        for idx in range(len(manager)):
            calculateTime(idx)
            
        return max(informTime)
