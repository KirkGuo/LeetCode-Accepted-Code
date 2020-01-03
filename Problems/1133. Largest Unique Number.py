class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = set()
        appear = set()
        for each in A:
            if each in appear:
                continue
            if each in cnt:
                appear.add(each)
                cnt.remove(each)
                continue
            cnt.add(each)
        
        return max(cnt) if cnt else -1
