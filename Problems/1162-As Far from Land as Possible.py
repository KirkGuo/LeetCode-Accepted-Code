class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        q = []
        reach = [[-1 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    q.append((i,j))
                    reach[i][j] = 0
        ret = -1
        while q:
            i, j = q.pop(0)
            if i>0 and grid[i-1][j]==0 and reach[i-1][j]==-1:
                reach[i-1][j] = reach[i][j] + 1
                ret = max(reach[i-1][j], ret)
                q.append((i-1,j))
            if i<rows-1 and grid[i+1][j]==0 and reach[i+1][j]==-1:
                reach[i+1][j] = reach[i][j] + 1
                ret = max(reach[i+1][j], ret)
                q.append((i+1,j))
            if j>0 and grid[i][j-1]==0 and reach[i][j-1]==-1:
                reach[i][j-1] = reach[i][j] + 1
                ret = max(reach[i][j-1], ret)
                q.append((i,j-1))
            if j<cols-1 and grid[i][j+1]==0 and reach[i][j+1]==-1:
                reach[i][j+1] = reach[i][j] + 1
                ret = max(reach[i][j+1], ret)
                q.append((i,j+1))
        return ret
