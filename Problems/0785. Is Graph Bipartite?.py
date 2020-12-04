class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        links = collections.defaultdict(set)
        
        for idx, ends in enumerate(graph):
            for e in ends:
                links[idx].add(e)
                links[e].add(idx)
        
        visit = {k: -1 for k in links.keys()}
        
        for each in links:
            if not self.bfs(each, links, visit):
                return False
        return True
        
        
    def bfs(self, start, links, visit):
        if visit[start] != -1:
            return True
        q = [(start, 0)]
        visit[start] = 0
        while q:
            curr, color = q.pop(0)
            for end in links[curr]:
                if visit[end] == -1:
                    visit[end] = 1 - color
                    q.append((end, 1 - color))
                elif visit[end] == color:
                    return False
        return True     
    
#     def dfs(self, curr, links, visit, flag):
#         if visit[curr] == 1 - flag:
#             return False
#         if visit[curr] == flag:
#             return True
        
#         visit[curr] = flag
        
#         for end in links[curr]:
#             if self.dfs(end, links, visit, 1-flag) and len(visit) == sum(visit.values()):
#                 return True
#         visit[curr] = -1
#         return False
        
        
