class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for each in strs:
            idx = ''.join(sorted(each))
            if idx not in ans:
                ans[idx] = []
            ans[idx].append(each)
        return [ans[each] for each in ans]
