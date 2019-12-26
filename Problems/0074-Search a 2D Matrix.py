class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        x, y = m-1, 0
        
        while x>=0 and y<n:
            if matrix[x][y]==target:
                return True
            if matrix[x][y]>target:
                x -= 1
            else:
                y += 1
        return False
