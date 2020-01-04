class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(target, idx, path):
            if target<0:
                return
            if target==0:
                ans.append(tuple(path))
                return
            
            for i in range(idx, len(candidates)):
                dfs(target-candidates[i], i+1, path+[candidates[i]])
        
        candidates.sort()
        dfs(target, 0, [])
        
        return [list(each) for each in set(ans)]
