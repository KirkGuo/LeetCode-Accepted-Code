class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = ['']
        for each in digits:
            ans = [each1+each2 for each1 in ans for each2 in num2letter[each]]
        return ans
