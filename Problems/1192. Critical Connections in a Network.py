class Solution:
    def __init__(self):
        # self.connecteds = []
        self.stack = []
        self.in_stack = set()
        self.dfn = None
        self.low = None
        self.adj = collections.defaultdict(set)
        self.cnt = 1
        self.ans = []
        self.parent = None
    
    def dfs(self, idx):
        self.dfn[idx] = self.low[idx] = self.cnt
        self.cnt += 1
        self.stack.append(idx)
        self.in_stack.add(idx)

        for each in self.adj[idx]:
            if not self.dfn[each]:
                self.parent[each] = idx
                self.dfs(each)
                if self.low[each]>self.dfn[idx]:
                    self.ans.append([idx, each])
                self.low[idx] = min(self.low[idx], self.low[each])
            elif self.parent[idx] != each:
                self.low[idx] = min(self.low[idx], self.dfn[each])

        # if self.low[idx]==self.dfn[idx]:
        #     self.connecteds.append(set())
        #     while self.stack:
        #         curr = self.stack.pop()
        #         self.in_stack.remove(curr)
        #         self.connecteds[-1].add(curr)
        #         if curr==idx:
        #             break
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.dfn = [0 for i in range(n)]
        self.low = [0 for i in range(n)]
        self.parent = [-1 for i in range(n)]
        
        for u, v in connections:
            self.adj[u].add(v)
            self.adj[v].add(u)
        self.dfs(0)
        return self.ans
