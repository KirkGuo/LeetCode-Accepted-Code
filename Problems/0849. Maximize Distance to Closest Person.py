class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats = seats[::-1]+seats+seats[::-1]
        curr = 0
        max_dist = 0
        for each in seats:
            if each:
                max_dist = max(max_dist, curr)
                curr = 0
            else:
                curr += 1
        return (max_dist+1)>>1
