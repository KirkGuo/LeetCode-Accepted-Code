class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        ret = 0
        for idx in range(len(A)):
            if not A[idx][0]:
                A[idx] = [1-each for each in A[idx]]
        for j in range(1,len(A[0])):
            cnt = 0
            for i in range(len(A)):
                if A[i][j]:
                    cnt -= 1
                else:
                    cnt += 1
            if cnt>0:
                for i in range(len(A)):
                    A[i][j] = 1 - A[i][j]
        for each in A:
            ret += int(''.join([str(num) for num in each]), 2)
        return ret
