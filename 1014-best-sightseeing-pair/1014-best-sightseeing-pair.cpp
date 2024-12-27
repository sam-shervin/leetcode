class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int a = values[0];
        int maxi = a;
        for(int i=1; i<values.size(); i++){
            maxi = max(maxi, a+values[i]-i);
            a = max(a, values[i]+i);
        }
        return maxi;
    }
};