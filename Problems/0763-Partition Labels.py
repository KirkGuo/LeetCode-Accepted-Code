class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        cnt = {}
        for idx, each in enumerate(S):
            if each not in cnt:
                cnt[each] = [idx, idx]
            else:
                cnt[each][1] = idx if idx > cnt[each][1] else cnt[each][1]
        dividers = []
        for each in cnt:
            if not dividers or cnt[each][0]>dividers[-1][1]:
                dividers.append(cnt[each])
            elif cnt[each][1]<=dividers[-1][1]:
                continue
            else:
                dividers[-1][1] = cnt[each][1]
        return [each[1]-each[0]+1 for each in dividers]
