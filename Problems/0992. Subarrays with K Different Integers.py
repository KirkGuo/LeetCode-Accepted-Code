class Solution:
    
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        n = len(A)
        
        w1 = collections.Counter()
        w2 = collections.Counter()
        flag1 = flag2 = 0
        
        ans = left1 = left2 = right = 0
        
        while right < n:
            val = A[right]
            
            w1[val] += 1
            w2[val] += 1
            if w1[val] == 1: flag1 += 1
            if w2[val] == 1: flag2 += 1
            
            while flag1 > K:
                w1[A[left1]] -= 1
                if w1[A[left1]] == 0: flag1 -= 1
                left1 += 1
            
            while flag2 >= K:
                w2[A[left2]] -= 1
                if w2[A[left2]] == 0: flag2 -= 1
                left2 += 1
            
            ans += left2 - left1
            right += 1
        
        return ans
        
        
    
            
        
