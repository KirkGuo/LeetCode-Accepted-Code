class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A = sorted(A)
        l = len(A)-1
        ans = -1
        for idx in range(len(A)):
            if A[idx]>=K:
                break
            left, right = idx+1, l
            while left<=right:
                mid = (left+right)//2
                curr = A[idx] + A[mid]
                if curr<K:
                    ans = curr if K-curr<K-ans else ans
                    left += 1
                else:
                    right -= 1
        return ans
