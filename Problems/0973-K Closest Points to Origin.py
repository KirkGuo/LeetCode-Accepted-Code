class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        for each in points:
            d = each[0]**2 + each[1]**2
            if d not in dist:
                dist[d] = []
            dist[d].append(each)
        ds = sorted(dist.keys())
        ans = []
        curr = 0
        for each in ds:
            if curr>=K:
                break
            ans += dist[each]
            curr += len(dist[each])
        return ans
