class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        chs = ''
        for each in S:
            if each!='-':
                chs += each
        ans = []
        while chs:
            ans.append(chs[-K:])
            chs = chs[:-K]
        return '-'.join(each.upper() for each in ans[::-1])
