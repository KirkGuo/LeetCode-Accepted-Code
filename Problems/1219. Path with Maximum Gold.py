class Solution:
    
    def dfs(self, m, n, x, y, gold, grid):
        if x<0 or x>=m or y<0 or y>=n:
            return gold
        if not grid[x][y]:
            return gold
        steps = [(0,1),(1,0),(0,-1),(-1,0)]
        ret = 0
        for step in steps:
            next_x, next_y = x+step[0], y+step[1]
            tmp = grid[x][y]
            grid[x][y] = 0
            ret = max(ret, self.dfs(m, n, next_x, next_y, gold+tmp, grid))
            grid[x][y] = tmp
        return ret
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(m, n, i, j, 0, grid))
        return ans
