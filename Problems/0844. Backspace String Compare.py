class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ''
        t = ''
        for each in S:
            if each == '#':
                s = s[:-1]
            else:
                s += each
        for each in T:
            if each == '#':
                t = t[:-1]
            else:
                t += each
        return s==t
