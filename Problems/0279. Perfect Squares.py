class Solution:
    def numSquares(self, n: int) -> int:
        bound = 1
        while bound**2 <= n:
            bound += 1
        q = []
        q.append([0, 0, 1])
        while q:
            sumed, ret, idx = q.pop(0)
            for i in range(idx, bound):
                curr = sumed + i**2
                if curr==n:
                    return ret+1
                if curr>n:
                    break
                q.append([curr, ret+1, i])
