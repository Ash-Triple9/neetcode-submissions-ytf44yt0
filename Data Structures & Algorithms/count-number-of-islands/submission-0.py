class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Given a 2d array, where 1 represents an island and 0 represents water.
        Count and return the number of islands.
        An island is formed by adjacent 1s where adjacent means horizontal or vertical

        You literally cannot do a brute force, have to know bfs/dfs
        
        '''
        if not grid:
            return 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            directions= [[1,0], [-1,0], [0,1], [0,-1]]
            q = collections.deque()
            q.append([r,c])
            while q:
                # pop the earliest set of r,c
                row, col = q.popleft()
                for dr, dc in directions:
                    nr=dr + row
                    nc=dc + col
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        q.append([nr,nc])
                        visited.add((nr,nc)) 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # starts off our recursive search
                    visited.add((r,c))
                    bfs(r,c)
                    islands+=1
        return islands