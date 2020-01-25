class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cnt = {}
        for id,val in items:
            if id not in cnt:
                cnt[id] = []
            cnt[id].append(val)
        ans = [[k,sum(sorted(v, reverse=True)[:5])//5] for k,v in cnt.items()]
        return sorted(ans)
