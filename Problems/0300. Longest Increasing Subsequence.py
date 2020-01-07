class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for idx, each in enumerate(nums):
            if idx==0:
                dp.append(1)
            else:
                l_max = 0
                for i in range(idx):
                    if nums[i]<nums[idx]:
                        l_max = max(l_max, dp[i])
                dp.append(l_max+1)
        return max(dp)
            
