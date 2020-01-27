class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        while s:
            curr = s[:2*k]
            s = s[2*k:]
            ans += curr[:k][::-1]
            ans += curr[k:]
        return ans
