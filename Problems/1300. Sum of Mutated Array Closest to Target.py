class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        curr_sum = sum(arr)
        if curr_sum <= target:
            return max(arr)
        
        arr = sorted(arr, key=lambda item: -item)
        
        n = len(arr)
        i = 0
        val = arr[i]
        
        
        while True:
            while i + 1 < n and arr[i] == arr[i+1]:
                i += 1
            if i == n - 1:
                break
            if curr_sum - (i + 1) * (arr[i] - arr[i+1]) > target:
                curr_sum -= (i + 1) * (arr[i] - arr[i+1])
                val = arr[i+1]
                i += 1
                continue
            else:
                break
            
        diff = curr_sum - target
        step = i + 1
        remain = diff % step
        if remain < step / 2:
            return val - diff // step
        return val - diff // step - 1
