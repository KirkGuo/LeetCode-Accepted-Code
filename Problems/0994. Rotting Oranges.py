class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rot = set()
        
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh.add((i,j))
                elif grid[i][j]==2:
                    rot.add((i,j))

        if fresh and not rot:
            return -1
        if not fresh:
            return 0

        while fresh:
            steps = [(0,1), (1,0), (0,-1), (-1,0)]
            nxts = set()
            for step in steps:
                for each in rot:
                    nxt = (each[0]+step[0], each[1]+step[1])
                    if nxt in fresh:
                        fresh.remove(nxt)
                        nxts.add(nxt)
            ans += 1
            if not nxts and fresh:
                return -1
            rot = rot.union(nxts)
        return ans
