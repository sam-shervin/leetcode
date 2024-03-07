class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        unordered_map<string, int> ruleIndices = {{"type", 0}, {"color", 1}, {"name", 2}};
        int index = ruleIndices[ruleKey];
        int count = 0;
        for (const auto& item : items) {
            if (item[index] == ruleValue) {
                count++;
            }
        }
        return count;
    }
};