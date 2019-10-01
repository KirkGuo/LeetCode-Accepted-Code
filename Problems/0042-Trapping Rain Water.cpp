class Solution {
public:
    int trap(vector<int>& height) {
        if(!height.size())
            return 0;
        int left = 0, right = height.size()-1;
        int left_bound = height[left], right_bound = height[right];
        int ans = 0;
        while(left<=right){
            if(left_bound<right_bound){
                height[left] > left_bound ? (left_bound = height[left]) : (ans += left_bound-height[left]);
                left++;
            }
            else{
                height[right] > right_bound ? (right_bound = height[right]) : (ans += right_bound-height[right]);
                right--;
            }
        }
        return ans;
    }
};
