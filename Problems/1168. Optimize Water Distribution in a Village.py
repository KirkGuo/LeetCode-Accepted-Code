class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        edges = {}
        for each in pipes:
            i, j, val = each
            i, j = i - 1, j - 1
            if i not in edges:
                edges[i] = []
            if j not in edges:
                edges[j] = []
            edges[i].append([j, val])
            edges[j].append([i, val])
        
        # candi_nodes = []
        # candi_edges = []
        
        candi_costs = []
        
        visit = [0 for each in range(n)]
        
        for idx, well in enumerate(wells):
            # heapq.heappush(candi_nodes, [well, idx])
            heapq.heappush(candi_costs, [well, idx])
        
        ans = 0
        
        while candi_costs:
            cost, idx = heapq.heappop(candi_costs)
            
            if visit[idx]:
                continue
            visit[idx] = 1
            
            ans += cost
            
            if idx not in edges:
                continue
            
            for target, val in edges[idx]:
                heapq.heappush(candi_costs, [val, target])
        
#         while candi_nodes:
#             val, idx = heapq.heappop(candi_nodes)
            
#             if visit[idx]:
#                 continue
#             visit[idx] = 1
#             ans += val
            
#             if idx not in edges:
#                 continue
            
#             for target, pipe in edges[idx]:
#                 heapq.heappush(candi_edges, [pipe, target])
                
#             while candi_edges:
#                 pipe, target = heapq.heappop(candi_edges)
#                 if visit[target]:
#                     continue
#                 visit[target] = 1
#                 ans += min(wells[target], pipe)
#                 for target_, pipe_ in edges[target]:
#                     heapq.heappush(candi_edges, [pipe_, target_])
        
        return ans
