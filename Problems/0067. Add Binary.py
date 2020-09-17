class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, base=2), int(b, base=2)
        output = a + b
        return f'{output:b}'
