class Solution:
    def jump(self, nums: List[int]) -> int:
        min_step = [0 for _ in nums]
        
        n = len(nums)
        idx = 1
        curr = 0
        
        while curr < n:
            while idx <= curr + nums[curr] and idx < n:
                if min_step[idx] == 0:
                    min_step[idx] = min_step[curr] + 1
                idx += 1
            curr += 1
        
        return min_step[-1]
