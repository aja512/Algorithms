class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            l, r = 0, len(grid[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            count += (len(grid[0]) - l)
        return count 
