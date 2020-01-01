class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        
        appears = set()
        
        last = {each:idx for idx, each in enumerate(s)}
        
        for idx, each in enumerate(s):
            if each not in appears:
                while stack and each < stack[-1] and idx < last[stack[-1]]:
                    appears.remove(stack.pop())
                stack.append(each)
                appears.add(each)
        return ''.join(stack)
        
