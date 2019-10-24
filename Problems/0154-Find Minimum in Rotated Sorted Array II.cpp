class Solution {
public:
    int findMin(vector<int>& nums) {
        int ans = nums[0];
        int start = 0, end = nums.size()-1;
        while(start<=end){
            int mid = (start+end)/2;
            ans = min(nums[mid], ans);
            if(nums[mid]<nums[end])
                end = mid-1;
            else if(nums[mid]>nums[start] &&nums[mid]>nums[end])
                start = mid+1;
            else if(nums[mid]==nums[start] && nums[mid]==nums[end]){
                for(int i=start; i<mid; i++)
                    if(nums[i]<ans)
                        return nums[i];
                start = mid+1;
            }
            else if(nums[mid]>nums[end])
                start = mid+1;
            else
                end = mid-1;
               
        }
        return ans;
    }
};
