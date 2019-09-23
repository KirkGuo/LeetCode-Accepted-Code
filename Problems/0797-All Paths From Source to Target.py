class node:
    def __init__(self, n=None, idx=None, nums=None):
        self.mask = [0 for i in range(nums)] if n==None else [each for each in n.mask]
        self.path = [] if n==None else [each for each in n.path]
        if idx != None:
            self.mask[idx] = 1
            self.path.append(idx)
        

class Solution:
    def __init__(self):
        self.ret = []
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        q = []
        if len(graph) == 0:
            return self.ret
        q.append(node(idx=0, nums=target+1))
        while len(q):
            tmp = q.pop(0)
            if(tmp.path[-1]==target):
                self.ret.append(tmp.path)
            else:
                for each in graph[tmp.path[-1]]:
                    if tmp.mask[each] == 0:
                        q.append(node(n=tmp, idx=each))
        return self.ret
