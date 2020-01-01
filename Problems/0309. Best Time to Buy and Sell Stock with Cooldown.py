class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0
        
        hs = -prices[0]
        nh = 0
        nh_cd = 0
        
        for price in prices:
            curr_hs = max(hs, nh_cd-price)
            curr_nh = max(hs+price, nh)
            hs = max(hs, curr_hs)
            nh_cd = nh
            nh = max(curr_nh, nh)
        
        return max(hs, nh)
