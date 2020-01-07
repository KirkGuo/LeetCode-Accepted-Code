class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums)<3:
            return False
        ans = []
        for num in nums:
            if len(ans)==3:
                return True
            if not ans:
                ans.append(num)
            else:
                if num>ans[-1]:
                    ans.append(num)
                else:
                    for i in range(len(ans)):
                        if num<=ans[i]:
                            ans[i] = num
                            break
        return True if len(ans)==3 else False
