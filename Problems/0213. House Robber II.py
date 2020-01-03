class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        ans = 0
        
        dp_r, dp_nr = 0, 0
        for idx in range(len(nums)):
            if idx==0:
                dp_r = nums[idx]
            elif idx==1:
                dp_nr = dp_r
            elif idx==len(nums)-1:
                ans = max(dp_r, dp_nr)
            else:
                curr_r = nums[idx] + dp_nr
                curr_nr = max(dp_r, dp_nr)
                dp_r, dp_nr = curr_r, curr_nr
        
        dp_r, dp_nr = 0, 0
        for idx in range(len(nums)):
            if idx==0:
                pass
            elif idx==1:
                dp_r = nums[idx]
            else:
                curr_r = dp_nr + nums[idx]
                curr_nr = max(dp_r, dp_nr)
                dp_r, dp_nr = curr_r, curr_nr
                if idx==len(nums)-1:
                    ans = max(ans, max(dp_r, dp_nr))
     
        return ans
