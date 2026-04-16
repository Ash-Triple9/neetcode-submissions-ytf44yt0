class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            # base case, check whether it's out of bounds or encountered a "0"
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c]==0:
                return 0 
            grid[r][c] = 0
            return (1 + dfs(r+1, c) +  dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r,c)
                maxArea = max(area, maxArea)
        return maxArea

        