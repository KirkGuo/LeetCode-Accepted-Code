class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 0
        ans = 0
        bitset = False
        for each in str:
            if each not in ' -+0123456789':
                break
            elif each==' ' and bitset:
                break
            elif each == '-':
                if bitset:
                    break
                sign = -1
                bitset = True
            elif each == '+':
                if bitset:
                    break
                sign = 1
                bitset = True
            elif each in '0123456789':
                ans = ans*10 + ord(each)-ord('0')
                bitset = True
        if sign == -1:
            ans = -ans
        if ans > 2**31-1:
            return 2**31-1
        if ans < -2**31:
            return -2**31
        return ans
