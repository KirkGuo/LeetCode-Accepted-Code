class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calc(n):
            ans = 0
            while n:
                dig = n%10
                ans += dig**2
                n //= 10
            return ans
        
        path = set()
        
        while n not in path:
            path.add(n)
            n = calc(n)
        if n == 1:
            return True
        return False
