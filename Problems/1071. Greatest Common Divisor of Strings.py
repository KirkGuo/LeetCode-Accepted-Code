class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1==str2:
            return str1
        if len(str1)>len(str2) and str2 in str1:
            return self.gcdOfStrings(str2, str1[len(str2):])
        if len(str1)<len(str2) and str1 in str2:
            return self.gcdOfStrings(str1, str2[len(str1):])
        return ''
