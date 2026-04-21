class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Definitely a multi source problem because more than one rotten fruit can progress at the same time
        Looks like an application of bfs
        Start by queuing up the rotten fruits,
            then do bfs on them, only queuing up fresh fruits and incrementing count
        '''
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        q= collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh +=1
        count = 0
        while q and fresh>0:
            s = len(q)
            for _ in range(s):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh-=1
            count+=1
        
        if fresh>0:
            print(fresh)
            return -1
        
        return count



        