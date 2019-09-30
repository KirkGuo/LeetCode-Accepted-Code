class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0]) if len(grid) else 0
        mask = [[0 for each in range(m)] for each in range(n)] 
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and mask[i][j]==0:
                    mask[i][j] = 1
                    ret += 1
                    q = [(i,j)]
                    while q:
                        x, y = q.pop(0)
                        if x<n-1 and grid[x+1][y]=='1' and mask[x+1][y]==0:
                            mask[x+1][y] = 1
                            q.append((x+1,y))
                        if y<m-1 and grid[x][y+1]=='1' and mask[x][y+1]==0:
                            mask[x][y+1] = 1
                            q.append((x, y+1))
                        if x and grid[x-1][y]=='1' and mask[x-1][y]==0:
                            mask[x-1][y] = 1
                            q.append((x-1,y))
                        if y and grid[x][y-1]=='1' and mask[x][y-1]==0:
                            mask[x][y-1] = 1
                            q.append((x,y-1))
        return ret
