class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp_r, dp_b, dp_g = 0, 0, 0
        
        for idx in range(len(costs)):
            curr_r = min(dp_b, dp_g) + costs[idx][0]
            curr_b = min(dp_r, dp_g) + costs[idx][1]
            curr_g = min(dp_r, dp_b) + costs[idx][2]
            
            dp_r, dp_b, dp_g = curr_r, curr_b, curr_g
        
        return min(dp_r, min(dp_g, dp_b))
