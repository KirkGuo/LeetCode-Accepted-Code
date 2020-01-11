class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = nums[0]
        dp_min = nums[0]
        
        ans = nums[0]
        for idx, each in enumerate(nums):
            if idx:
                if each>=0:
                    dp_max, dp_min = max(each, dp_max*each), min(each, dp_min*each)
                else:
                    dp_max, dp_min = max(each, dp_min*each), min(each, dp_max*each)
                ans = max(ans, dp_max)
        return ans
