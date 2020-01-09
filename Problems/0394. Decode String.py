class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        for each in s:
            if each ==']':
                curr = []
                ch = stack.pop()
                while ch!='[':
                    curr.append(ch)
                    ch = stack.pop()
                curr = curr[::-1]
                n = []
                while stack and ord('0')<=ord(stack[-1])<=ord('9'):
                    n.append(stack.pop())
                n = int(''.join(n[::-1]))
                stack += n*curr
            else:
                stack.append(each)
        
        return ''.join(stack)
