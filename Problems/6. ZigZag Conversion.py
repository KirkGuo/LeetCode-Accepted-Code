class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result_map = [['' for _ in range(len(s))]  for _ in range(numRows)]
        x, y = 0, 0
        idx = 0
        nxt_x, nxt_y = 1, 0
        while idx < len(s):
            result_map[x][y] = s[idx]
            x, y = x + nxt_x, y + nxt_y
            idx += 1
            if x == 0:
                nxt_x, nxt_y = 1, 0
            elif x == numRows - 1:
                nxt_x, nxt_y = -1, 1
        
        result = ''.join([''.join(each) for each in result_map])
        return result
