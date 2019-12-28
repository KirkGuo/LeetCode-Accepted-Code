class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        ans = [each for each in str(x)]
        return ans == ans[::-1]
