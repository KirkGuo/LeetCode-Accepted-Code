class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        for step in range(2, n+1):
            if n%step==0:
                return step+self.minSteps(n//step)  
