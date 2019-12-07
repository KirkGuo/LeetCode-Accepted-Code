class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='0':
                    matrix[i][j] = 0
                elif i==0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + 1
        ans = 0
        for i in range(len(matrix)):
            stack = [-1]
            for j in range(len(matrix[i])):
                while stack[-1]!=-1 and matrix[i][stack[-1]] > matrix[i][j]:
                    height = matrix[i][stack.pop(-1)]
                    tmp_sqr = height * (j - stack[-1] - 1)
                    ans = max(tmp_sqr, ans)
                stack.append(j)
            while stack[-1]!=-1:
                height = matrix[i][stack.pop(-1)]
                tmp_sqr = height * (j - stack[-1])
                ans = max(tmp_sqr, ans)

        return ans
                    
