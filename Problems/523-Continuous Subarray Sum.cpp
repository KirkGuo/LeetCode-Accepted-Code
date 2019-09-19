class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        if(nums.size()<2)
            return false;
        if(k==0){
            for(int i=0; i<nums.size()-1; i++)
                if(!nums[i] && !nums[i+1])
                    return true;
            return false;
        }
        for(int i=0; i<nums.size()-1; i++)
            if(!nums[i] && !nums[i+1])
                return true;
        set<int> reminders;
        int sum = 0;
        for(int i=0; i<nums.size(); i++){
            sum += nums[i];
            if(i && sum%k==0)
                return true;
            if(nums[i]%k!=0 && reminders.find(sum%k)!=reminders.end())
                return true;
            reminders.insert(sum%k);
        }
        return false;                
    }
};
