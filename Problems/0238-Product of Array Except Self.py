class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for each in nums:
            if each==0:
                zeros += 1
                continue
            prod *= each
        if zeros > 1:
            return [0 for each in nums]
        if zeros == 1:
            return [0 if each else prod for each in nums]
        return [prod//each for each in nums]
