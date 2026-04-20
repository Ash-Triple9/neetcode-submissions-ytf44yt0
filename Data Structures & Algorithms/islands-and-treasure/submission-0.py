class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Something we can do is instead of trying to reach the treasure chest
         from all other spaces, try to start from the treasure spaces and reach other islands, updating each space by the minimum number
        To do that, we first have to identify the treasure spaces
        They are only allowed to move up down left and right
        We can incorporate a bfs starting from the treasure space,
            For that treasure space, every successful space we can traverse is one space away from the treasure. 
        '''
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                   q.append([r,c])
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]== 2147483647:
                    grid[nr][nc] = min(grid[nr][nc], grid[r][c] + 1)
                    q.append([nr,nc])


        

        