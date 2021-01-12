class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        self.m = m
        self.n = n
        
        self.mem = [[[-1, -1] for _ in range(n)] for _ in range(m)]
        self.num_island = 0
        
        ans = []
        
        for i, j in positions:
            self.update(i, j)
            ans.append(self.num_island)
            
        return ans
    
    def update(self, i, j):
        
        if self.mem[i][j] != [-1, -1]:
            return
        
        adj_island = self.adj(i, j)
        
        if not adj_island:
            self.num_island += 1
            self.mem[i][j] = [i, j]
            return
        
        father = self.get_father(adj_island[0])
        self.mem[i][j] = father
        
        if len(adj_island) == 1:
            return
        
        num_father = len(set([tuple(self.get_father(each)) for each in adj_island]))
        
        for next_pos in adj_island[1:]:
            self.update_father(next_pos, father)
        
        self.num_island -= num_father - 1
        
        return
    
    def adj(self, i, j):
        
        adj_lands = []
        
        for ci, cj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj  = i + ci, j + cj
            if 0<=ni<self.m and 0<=nj<self.n and self.mem[ni][nj] != [-1, -1]:
                adj_lands.append([ni,nj])
        
        return adj_lands
    
    def get_father(self, pos):
        i, j = pos
        if self.mem[i][j] == [i, j]:
            return self.mem[i][j]
        
        return self.get_father(self.mem[i][j])
    
    def update_father(self, pos, father):
        i, j = pos
        if self.mem[i][j] == [i, j]:
            self.mem[i][j] = father
            return
        
        self.update_father(self.mem[i][j], father)
        self.mem[i][j] = father
        return
            
