class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remain = 0
        ans = ''
        for each in s:
            if each==')':
                if remain:
                    remain -= 1
                    ans += each
            elif each=='(':
                remain += 1
                ans += each
            else:
                ans += each
        ret = ''
        for each in ans[::-1]:
            if each == '(' and remain:
                remain -= 1
            else:
                ret += each
        return ret[::-1]
