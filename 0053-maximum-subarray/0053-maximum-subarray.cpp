class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = INT_MIN;
        int sum = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]>nums[i]+sum){
                sum = nums[i];
            }else{
                sum = nums[i]+sum;
            }
            if(sum>max_sum){
                max_sum = sum;
            }
        }
        return max_sum;
    }
};