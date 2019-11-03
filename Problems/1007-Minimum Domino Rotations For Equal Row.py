class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ans = -1
        same = A[0]
        curr = 0
        for i in range(len(A)):
            if A[i]!=same and B[i]!=same:
                curr = -1
                break
            if A[i]!=same:
                curr += 1
        if curr!=ans and curr!=-1:
            ans = curr if ans==-1 else min(ans, curr)
        curr = 0
        for i in range(len(B)):
            if B[i]!=same and A[i]!=same:
                curr = -1
                break
            if B[i]!=same:
                curr += 1
        if curr!=ans and curr!=-1:
            ans = curr if ans==-1 else min(ans, curr)
        
        same = B[0]
        curr = 0
        for i in range(len(A)):
            if A[i]!=same and B[i]!=same:
                curr = -1
                break
            if A[i]!=same:
                curr += 1
        if curr!=ans and curr!=-1:
            ans = curr if ans==-1 else min(ans, curr)
        curr = 0
        for i in range(len(B)):
            if B[i]!=same and A[i]!=same:
                curr = -1
                break
            if B[i]!=same:
                curr += 1
        if curr!=ans and curr!=-1:
            ans = curr if ans==-1 else min(ans, curr)
        return ans
