class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        q = []
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    q.append([0,i,j])
        steps = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            val, x, y = q.pop(0)
            for step in steps:
                nxt = [x+step[0], y+step[1]]
                if 0<=nxt[0]<m and 0<=nxt[1]<n and rooms[nxt[0]][nxt[1]]==2147483647:
                    rooms[nxt[0]][nxt[1]] = val + 1
                    q.append([val+1, nxt[0], nxt[1]])
        return
                    
