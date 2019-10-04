class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31-1, -2**32
        sign = True
        if x<0:
            sign = False
            x = -x
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        if ans>INT_MAX or ans<INT_MIN:
            return 0
        return ans if sign else -ans
