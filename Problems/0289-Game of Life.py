class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def cntNeighbor(x, y, m, n):
            type_cell = {1:1, 0:0, -1:0, -2:1}
            ans = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i<0 or i>=m or j<0 or j>=n or (i==x and j==y):
                        continue
                    ans += type_cell[board[i][j]]
            return ans
        
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                neighbor = cntNeighbor(x, y, m, n)
                if board[x][y]==1 and (neighbor<2 or neighbor>3):
                    board[x][y] = -2
                elif board[x][y]==0 and neighbor==3:
                    board[x][y] = -1
        for x in range(m):
            for y in range(n):
                if board[x][y] == -1:
                    board[x][y] = 1
                elif board[x][y] == -2:
                    board[x][y] = 0
