class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(remain, curr, path):
            if remain<0:
                return
            if remain==0:
                ans.append(path)
                return
            for idx in range(curr, len(candidates)):
                dfs(remain-candidates[idx], idx, path+[candidates[idx]])
            
        
        candidates.sort()
        dfs(target, 0, [])
        return ans
