class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        if n <= 1:
            return 0
        m = len(heightMap[0])
        visit = [[0 for _ in heightMap[0]] for _ in heightMap]
        
        min_heap = []
        
        water = 0
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visit[i][j] = 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            
            h, x, y = heapq.heappop(min_heap)
            
            for dx, dy in directions:
                cx, cy = x + dx, y + dy
                if 0 <= cx < n and 0 <= cy < m and not visit[cx][cy]:
                    curr_h = heightMap[cx][cy]
                    water += max(0, h - curr_h)
                    heapq.heappush(min_heap, (max(curr_h, h), cx, cy))
                    visit[cx][cy] = 1
        
        return  water
        
            
