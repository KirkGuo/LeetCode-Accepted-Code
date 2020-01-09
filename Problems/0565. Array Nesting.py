class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0 for each in nums]
        
        ans = 0
        
        for idx, each in enumerate(nums):
            if not visited[idx]:
                curr = 0
                step = idx
                while not visited[step]:
                    visited[step] = 1
                    curr += 1
                    step = nums[step]
                ans = max(curr, ans)
        
        return ans
