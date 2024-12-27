class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxi = values[0];
        for(int i=1; i<values.size(); i++){
            maxi = max(maxi, values[0]+values[i]-i);
            values[0] = max(values[0], values[i]+i);
        }
        return maxi;
    }
};