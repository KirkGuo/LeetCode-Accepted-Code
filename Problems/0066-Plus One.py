class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for each in digits:
            num *= 10
            num += each
        num += 1
        ans = []
        while num:
            ans.append(num%10)
            num //= 10
        return ans[::-1]
