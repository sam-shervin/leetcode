class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int maxi = *max_element(nums.begin(), nums.end());
        int su = 0;
        for(int i=0; i<k; i++){
            su = su + maxi + i;
        }
        return su;
    }
};