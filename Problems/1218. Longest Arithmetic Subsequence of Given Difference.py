class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0
        
        ans = -float('inf')
        mem = {}
        
        for each in arr:
            target = each - difference
            if target in mem:
                mem[each] = mem[target] + 1
            else:
                mem[each] = 1
            ans = max(ans, mem[each])
                
        return ans
