class Solution:
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        mem = collections.defaultdict(int)
        for a in A:
            for b in B:
                mem[a+b] += 1
        ans = 0
        for c in C:
            for d in D:
                if -(c+d) in mem:
                    ans += mem[-(c+d)]
        return ans
        
