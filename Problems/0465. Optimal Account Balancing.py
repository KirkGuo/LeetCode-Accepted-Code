class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        debt = collections.defaultdict(int)
        for x, y, z in transactions:
            debt[x] += z
            debt[y] -= z
        debts = [debt[each] for each in debt if debt[each]]
        return self.helper(debts)

    def helper(self, debts):
        if not debts:
            return 0
        l = len(debts)
        n = 1 << l
        best = float('inf')
        for i in range(1, n-1):
            if self.fesiable(debts, i):
                left, right = self.divide(debts, i, l)
                curr = self.helper(left) + self.helper(right)
                best = min(curr, best)
        return min(l - 1, best)
    
    def fesiable(self, nums, i):
        sums = 0
        idx = 0
        while i:
            curr = i & 1
            i >>= 1
            if curr:
                sums += nums[idx]
            idx += 1
        return sums == 0
    
    def divide(self, debts, i, l):
        left = []
        right = []
        for j in range(l):
            curr = i & 1 << j
            if curr:
                left.append(debts[j])
            else:
                right.append(debts[j])
        return left, right
        
