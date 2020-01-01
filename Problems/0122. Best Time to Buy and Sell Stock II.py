class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        for idx in range(1, len(prices)):
            if prices[idx]>prices[idx-1]:
                ans += prices[idx]-prices[idx-1]
        return ans
