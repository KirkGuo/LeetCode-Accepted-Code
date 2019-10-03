class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums)<3 or nums[0]>0 or nums[-1]<0:
            return []
        cnt = collections.defaultdict(int)
        for each in nums:
            cnt[each] += 1
        ans = set()
        keys = [each for each in cnt]
        print(keys)
        print(cnt)
        for i in range(len(keys)):
            if keys[i]>0:
                break
            for k in range(len(keys)-1, i-1, -1):
                if keys[k]<0:
                    break
                target = -keys[i]-keys[k]
                if target not in cnt:
                    continue
                if (target==keys[i] and cnt[keys[i]]==1) or (target==keys[k] and cnt[keys[k]]==1):
                    continue
                if (target==keys[i]==keys[k] and cnt[target]<3):
                    continue
                a = min(keys[i], target)
                c = max(keys[k], target)
                b = 0 - a - c
                ans.add((a, b, c))
        return [list(each) for each in ans]
